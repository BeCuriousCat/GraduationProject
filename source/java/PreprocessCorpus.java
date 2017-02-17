package com.process;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.Reader;
import java.math.MathContext;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PreprocessCorpus {
	public static void main(String[] args) {
		PreprocessCorpus p = new PreprocessCorpus();
		p.process("G:/Myeclipse10.0/Graduate/src/source/a.txt");
	}

	/**
	 * 读取原始语料库按句分割获得：句子和标点的文本
	 * 
	 * @param fName
	 */
	public void process(String fPath) {
		BufferedReader bf = null;
		BufferedWriter fox = null;
		BufferedWriter foy = null;

		String fName = fPath.substring(fPath.lastIndexOf('/')+1,fPath.length()-4);
		String path = fPath.substring(0, fPath.lastIndexOf('/')+1);
		System.out.println(fName+" "+path);
		Pattern pattern = Pattern.compile("(.+?)(\\p{P})+"	);

		try {
			InputStream f = new FileInputStream(fPath);
			bf = new BufferedReader(new InputStreamReader(f));
			
			fox = new BufferedWriter(new FileWriter(path+fName+"_x"+".txt"));
			foy = new BufferedWriter(new FileWriter(path+fName+"_y"+".txt"));
			
			String line = bf.readLine();
			while (line != null) {

				Matcher matcher = pattern.matcher(line);

				boolean t = matcher.find();
				// System.out.println(t+line);
				while (t) {
					fox.write(matcher.group(1));
					fox.newLine();
					foy.write(matcher.group(2));
					foy.newLine();
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
}
