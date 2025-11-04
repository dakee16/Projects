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

import Entry.ClassEntry;
import Main.DBConnection;

/**
 *
 * @author daksh
 */
public class ClassQueries {
    private static Connection connection = null;
    private static PreparedStatement addclassStatement = null;
    private static PreparedStatement getAllCourseCodesStatement = null;
    private static PreparedStatement getClassSeatsStatement = null;
    private static PreparedStatement deleteClassStatement = null;

    private static ArrayList<String> courseList = new ArrayList<String>();
    private static ResultSet resultSet;

    public static void addClass(ClassEntry classEntry) {
        connection = DBConnection.getConnection();

        try {
            String addClassQuery = "INSERT INTO app.class (semester, coursecode, seats) VALUES (?, ?, ?)";
            addclassStatement = connection.prepareStatement(addClassQuery);
            addclassStatement.setString(1, classEntry.getSemester());
            addclassStatement.setString(2, classEntry.getCourseCode());
            addclassStatement.setInt(3, classEntry.getSeats());

            addclassStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static ArrayList<String> getAllCourseCodes(String semester) {
        connection = DBConnection.getConnection();
        courseList = new ArrayList<String>();

        try {
            String getAllCourseQuery = "SELECT coursecode FROM app.class WHERE semester = ?";
            getAllCourseCodesStatement = connection.prepareStatement(getAllCourseQuery);
            getAllCourseCodesStatement.setString(1, semester);
            resultSet = getAllCourseCodesStatement.executeQuery();

            while (resultSet.next()) {
                String courseCode = resultSet.getString("coursecode");
                courseList.add(courseCode);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return courseList;
    }

    public static int getClassSeats(String semester, String courseCode) {
        connection = DBConnection.getConnection();
        int seat = -1;

        try {
            String getClassSeatsQuery = "SELECT seats FROM app.class WHERE semester = ? AND coursecode = ?";
            getClassSeatsStatement = connection.prepareStatement(getClassSeatsQuery);
            getClassSeatsStatement.setString(1, semester);
            getClassSeatsStatement.setString(2, courseCode);
            ResultSet resultSet = getClassSeatsStatement.executeQuery();

            if (resultSet.next()) {
                seat = resultSet.getInt("seats");
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return seat;
    }

    public static void dropClass(String semester, String courseCode) {
        connection = DBConnection.getConnection();

        try {
            String deleteClassQuery = "DELETE FROM APP.CLASS WHERE semester = ? and coursecode = ? ";
            deleteClassStatement = connection.prepareStatement(deleteClassQuery);
            deleteClassStatement.setString(1, semester);
            deleteClassStatement.setString(2, courseCode);

            deleteClassStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

}
