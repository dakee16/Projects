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

import Entry.CourseEntry;
import Main.DBConnection;

/**
 *
     * @author daksh
 */

public class CourseQueries {
    private static Connection connection = null;
    private static PreparedStatement addCourseStatement = null;
    private static PreparedStatement getAllCourseCodesStatement = null;

    private static ArrayList<String> courseList = new ArrayList<String>();
    private static ResultSet resultSet;

    public static void addCourse(CourseEntry course) {
        connection = DBConnection.getConnection();

        try {
            String addCourseQuery = "INSERT INTO app.course (coursecode, description) VALUES (?, ?)";
            addCourseStatement = connection.prepareStatement(addCourseQuery);
            addCourseStatement.setString(1, course.getCourseCode());
            addCourseStatement.setString(2, course.getCourseDescription());            

            addCourseStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static ArrayList<String> getAllCourseCodes() {
        connection = DBConnection.getConnection();
        courseList = new ArrayList<String>();

        try {
            String getAllCourseQuery = "SELECT coursecode FROM app.course";
            getAllCourseCodesStatement = connection.prepareStatement(getAllCourseQuery);
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

}

