import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
	public static void main(String[] args) {
		PreprocessCorpus pc = new PreprocessCorpus();
		String fPath = "/home/chenzewei/GraduationProject/corpus/The_three_body.txt";
		if (args.length >= 1) {
			fPath = args[0];
		}

		if(fPath == null || fPath.length() == 0) {
			System.out.println("File Path is illegal");
		}
		else{
			pc.replace(fPath);
			fPath = "/home/chenzewei/GraduationProject/corpus/The_three_body_replace.txt";
			pc.process(fPath);
		}

	}
}
