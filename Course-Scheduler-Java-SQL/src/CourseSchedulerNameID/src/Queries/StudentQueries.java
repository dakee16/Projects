package Queries;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import Entry.StudentEntry;
import Main.DBConnection;

/**
 *
 * @author daksh
 */
public class StudentQueries {
    private static Connection connection = null;
    private static PreparedStatement addStudentStatement = null;
    private static PreparedStatement getAllStudentStatement = null;
    private static PreparedStatement getStudentIDStatement = null;
    private static PreparedStatement getStudentStatement = null;
    private static PreparedStatement deleteStudentStatement = null;

    private static ArrayList<StudentEntry> studentList = new ArrayList<StudentEntry>();
    private static StudentEntry student = null;
    private static ResultSet resultSet;

    public static void addStudent(StudentEntry student) {
        connection = DBConnection.getConnection();

        try {
            String addStudentQuery = "INSERT INTO app.student (studentid, firstname, lastname) VALUES (?, ?, ?)";
            addStudentStatement = connection.prepareStatement(addStudentQuery);
            addStudentStatement.setString(1, student.getStudentID());
            addStudentStatement.setString(2, student.getFirstName());
            addStudentStatement.setString(3, student.getLastName());

            addStudentStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static ArrayList<StudentEntry> getAllStudents() {
        connection = DBConnection.getConnection();
        studentList = new ArrayList<StudentEntry>();

        try {
            String getAllStudentQuery = "SELECT * FROM app.student";
            getAllStudentStatement = connection.prepareStatement(getAllStudentQuery);
            resultSet = getAllStudentStatement.executeQuery();

            while (resultSet.next()) {
                StudentEntry rowStudentEntry = new StudentEntry(resultSet.getString("studentid"),
                        resultSet.getString("firstname"), resultSet.getString("lastname"));
                studentList.add(rowStudentEntry);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return studentList;
    }

    public static String getStudentID(String fullName) {
        connection = DBConnection.getConnection();
        String studentId = null;

        String[] nameParts = fullName.split(", ");
        String lastName = nameParts[0];
        String firstName = nameParts[1];

        try {
            String query = "SELECT studentid FROM app.student WHERE firstname = ? AND lastname = ?";
            getStudentIDStatement = connection.prepareStatement(query);
            getStudentIDStatement.setString(1, firstName);
            getStudentIDStatement.setString(2, lastName);
            resultSet = getStudentIDStatement.executeQuery();

            if (resultSet.next()) {
                studentId = resultSet.getString("studentid");
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return studentId;
    }

    public static StudentEntry getStudent(String studentID) {
        connection = DBConnection.getConnection();

        try {
            String getStudentQuery = "SELECT * FROM app.student WHERE studentid = ?";
            getStudentStatement = connection.prepareStatement(getStudentQuery);
            getStudentStatement.setString(1, studentID);
            resultSet = getStudentStatement.executeQuery();

            while (resultSet.next()) {
                student = new StudentEntry(resultSet.getString("studentid"),
                        resultSet.getString("firstname"), resultSet.getString("lastname"));
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
        return student;
    }

    public static void dropStudent(String studentID) {
        connection = DBConnection.getConnection();

        try {
            String deleteStudentQuery = "DELETE FROM APP.STUDENT WHERE studentid = ?";
            deleteStudentStatement = connection.prepareStatement(deleteStudentQuery);
            deleteStudentStatement.setString(1, studentID);

            deleteStudentStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

    }

}
