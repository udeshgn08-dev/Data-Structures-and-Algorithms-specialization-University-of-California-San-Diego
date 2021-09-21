package com.string;

public class concat {

	public static void main(String[] args) {
		String firstName = "Udesh";
		String middleName = "kumar";
		String surName = "Ganesan";
		System.out.println(firstName + middleName + " " +surName);
		System.out.println(firstName.concat("")+ middleName.concat(" ").concat(surName));

	}

}
