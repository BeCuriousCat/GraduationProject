import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PreprocessCorpus {
	private static String[] clabels = {"，","！","；","：","（","）","——","……","—","·","《","》","。","、","“","”","‘","’",};
	
	private static String[] elabels = {",","!",";",":","(",")"};

/*	public static void main(String[] args) {
		PreprocessCorpus p = new PreprocessCorpus();
		p.process("G:/Myeclipse10.0/Graduate/src/source/a.txt");
	}*/

	/**
	 * 处理文件得到：句子和标点的ｔｘｔ文本
	 * 
	 * @param fName
	 */
	public void process(String fPath) {
		BufferedReader bf = null;
		BufferedWriter fox = null;
		BufferedWriter foy = null;
		
		HashSet<String> hs = new HashSet<String>();
		for (int i = 0; i < clabels.length; i++) {
			hs.add(clabels[i]);
		}
		
		String fName = fPath.substring(fPath.lastIndexOf('/')+1,fPath.length()-4);
		String path = fPath.substring(0, fPath.lastIndexOf('/')+1);
//		System.out.println(fName+" "+path);
		Pattern pattern = Pattern.compile("(.+?)(\\p{P})+"	);

		try {
			InputStream f = new FileInputStream(fPath);
			bf = new BufferedReader(new InputStreamReader(f));
			
			fox = new BufferedWriter(new FileWriter(path+fName+"_x"+".txt"));
			foy = new BufferedWriter(new FileWriter(path+fName+"_y"+".txt"));
			
			String line = bf.readLine();
			while (line != null) {
				//如果句子为空，弃用
				//除去两边的空格
				Matcher matcher = pattern.matcher(line.trim());
				boolean t = matcher.find();
				//System.out.println(t+line);
				while (t) {
					//如果标点不在常用中文标点中，则弃用
				if(hs.contains(matcher.group(2)) && !matcher.group(1).matches("\\s")){
						fox.write(matcher.group(1));
						fox.newLine();
						foy.write(matcher.group(2));
						foy.newLine();
					}
					t = matcher.find();
				}

				line = bf.readLine();
			}
		} catch (Exception e) {
			System.out.println("Preprocess Corpus Error!");
		} finally {
			try {
				bf.close();
				fox.close();
				foy.close();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	/**
	 * 将 英文标点替换成中文标点
	 * @param fPath
	 */
	public void replace(String fPath){
		BufferedReader bf = null;
		BufferedWriter bw = null;
		
		String fName = fPath.substring(fPath.lastIndexOf('/')+1,fPath.length()-4);
		String path = fPath.substring(0, fPath.lastIndexOf('/')+1);
				
		try {
			bf = new BufferedReader(new FileReader(fPath));
			bw = new BufferedWriter(new FileWriter(path+fName+"_replace"+".txt"));
			String line = bf.readLine();
			while(line != null){
				System.out.println(line);
				for (int i = 0; i < elabels.length; i++) {
					line = line.replace(elabels[i], clabels[i]);
				}
	//			System.out.println(line);
				bw.write(line);
				bw.newLine();
				line = bf.readLine();
			}
		} catch (Exception e) {
			System.out.println("translate English punctation to chinese error!");
			e.printStackTrace();
		}finally{
			try {
				bf.close();
				bw.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
