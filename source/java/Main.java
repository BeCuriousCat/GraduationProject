import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
	public static void main(String[] args) {
		PreprocessCorpus pc = new PreprocessCorpus();
		String path = "/home/chenzewei/GraduationProject/corpus/";
		String name = "The_three_body";
		String fPath = path+name+".txt";
		if (args.length >= 1) {
			name = args[0];
			fPath = path + name +".txt";
		}

		if(fPath == null || fPath.length() == 0) {
			System.out.println("File Path is illegal");
		}
		else{
			pc.replace(fPath);
			fPath = path+name+"_replace.txt";
			pc.process(fPath);
		}

	}
}
