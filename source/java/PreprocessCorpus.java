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
	private static String[] clabels = {"，","！","；","："
		,"（","）","——","……","—","·","《","》","。","、","“","”","‘","’",};
	private static String[] elabels = {",","!",";",":"
		,"(",")"};
	
	private static BufferedReader bf = null;
	private static BufferedWriter fox = null;
	private static BufferedWriter foy = null;
	private static BufferedWriter bw = null;
	private static String fName;
	private static String path;
	
/*	public static void main(String[] args) {
		PreprocessCorpus p = new PreprocessCorpus();
		p.process("G:/Myeclipse10.0/Graduate/src/source/a.txt");
	}*/

	/**
	 * 读取原始语料库按句分割获得：句子和标点的文本
	 * 暂时不考虑！”连用的情况只取！
	 * 有进一步改成标点结合的想法
	 * @param fName
	 */
	public void process(String fPath) {

		
		HashSet<String> hs = new HashSet<String>();
		for (int i = 0; i < clabels.length; i++) {
			hs.add(clabels[i]);
		}
		
		getPathName(fPath);
		
		System.out.println(fName+" "+path);
		Pattern pattern = Pattern.compile("([^　 \\p{P}]+?)(\\p{P})");

		try {
			InputStream f = new FileInputStream(fPath);
			bf = new BufferedReader(new InputStreamReader(f));
			
			fox = new BufferedWriter(new FileWriter(path+fName+"_x"+".txt"));
			foy = new BufferedWriter(new FileWriter(path+fName+"_y"+".txt"));
			
			String line = bf.readLine();
			while (line != null) {
				//除去两边的空格
				Matcher matcher = pattern.matcher(line.trim());
				boolean t = matcher.find();
				//System.out.println(t+line);
				while (t) {
					
					
					//#如果句子为空，弃用
					//如果标点不在常用中文标点中，则弃用
					if(hs.contains(matcher.group(2))){
						fox.write(matcher.group(1));
						System.out.println(matcher.group(1)+" "+matcher.groupCount()+matcher.group(2));
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
	 * 去除空白行并将 英文标点替换成中文标点
	 * @param fPath
	 */
	public void replace(String fPath){
		
		
		getPathName(fPath);
				
		try {
			bf = new BufferedReader(new FileReader(fPath));
			bw = new BufferedWriter(new FileWriter(path+fName+"_replace"+".txt"));
			String line = bf.readLine();
			while(line != null){
				System.out.println(line);
				for (int i = 0; i < elabels.length; i++) {
					line = line.replace(elabels[i], clabels[i]);
				}
				//System.out.println(line);
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
	/**
	 * 通过fPath获得Path和FileName
	 * @param fPath
	 */
	private void getPathName(String fPath) {
		fName = fPath.substring(fPath.lastIndexOf('/')+1,fPath.length()-4);
		path = fPath.substring(0, fPath.lastIndexOf('/')+1);
	}
}
