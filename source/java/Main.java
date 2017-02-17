package com.process;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Main {
	public static void main(String[] args) {
		PreprocessCorpus pc = new PreprocessCorpus();
		String fPath = "";
		if (args != null) {
			fPath = args[0];
		}

		if(fPath == null || fPath.length() == 0)
			System.out.println("File Path is illegal");
		else
			pc.process(fPath);
	}
}
