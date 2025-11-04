package Queries;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import Main.DBConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.sql.SQLException;

import Entry.ClassDescription;
import Entry.StudentEntry;
import Main.DBConnection;

/**
 *
 * @author daksh
 */
public class MultiTableQueries {
    private static Connection connection = null;
    private static PreparedStatement getAllClassDescStatement = null;
    private static PreparedStatement allScheduledStudentStatement = null;
    private static PreparedStatement allWaitlistedStudentStatement = null;
    private static PreparedStatement getDescStatement = null;
    private static PreparedStatement getStudentIDStatement = null;

    private static ArrayList<ClassDescription> allClassDesc = new ArrayList<ClassDescription>();
    private static ArrayList<StudentEntry> allScheduledStudent = new ArrayList<StudentEntry>();
    private static ArrayList<StudentEntry> allWaitlistedStudent = new ArrayList<StudentEntry>();
    private static ResultSet resultSet;

    public static ArrayList<ClassDescription> getAllClassDescriptions(String semester) {

        connection = DBConnection.getConnection();
        allClassDesc = new ArrayList<ClassDescription>();

        try {
            String getAllClassDescQuery = "SELECT * FROM app.class WHERE semester = ?";
            getAllClassDescStatement = connection.prepareStatement(getAllClassDescQuery);
            getAllClassDescStatement.setString(1, semester);

            resultSet = getAllClassDescStatement.executeQuery();

            while (resultSet.next()) {
                String courseCode = resultSet.getString("coursecode");
                String getDescQuery = "SELECT description FROM app.course WHERE coursecode = ?";
                getDescStatement = connection.prepareStatement(getDescQuery);
                getDescStatement.setString(1, courseCode);

                ResultSet descResultSet = getDescStatement.executeQuery();
                descResultSet.next();

                ClassDescription rowClassDesc = new ClassDescription(courseCode,
                        descResultSet.getString("description"),
                        resultSet.getInt("seats"));
                allClassDesc.add(rowClassDesc);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allClassDesc;
    }

    public static ArrayList<StudentEntry> getScheduledStudentsByClass(String semester, String courseCode) {
        connection = DBConnection.getConnection();
        allScheduledStudent = new ArrayList<StudentEntry>();

        try {
            String getAllScheduledStudentQuery = "SELECT studentid FROM APP.SCHEDULE Where semester = ? and Coursecode = ? and status ='Scheduled'";

            allScheduledStudentStatement = connection.prepareStatement(getAllScheduledStudentQuery);
            allScheduledStudentStatement.setString(1, semester);
            allScheduledStudentStatement.setString(2, courseCode);

            resultSet = allScheduledStudentStatement.executeQuery();

            while (resultSet.next()) {
                String studentid = resultSet.getString("studentid");
                String getDescQuery = "SELECT * FROM app.student WHERE studentid = ?";
                getStudentIDStatement = connection.prepareStatement(getDescQuery);
                getStudentIDStatement.setString(1, studentid);

                ResultSet studentIDResultSet = getStudentIDStatement.executeQuery();
                studentIDResultSet.next();

                StudentEntry rowStudentID = new StudentEntry(studentid, studentIDResultSet.getString("firstname"),
                        studentIDResultSet.getString("lastname"));
                allScheduledStudent.add(rowStudentID);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allScheduledStudent;
    }


    public static ArrayList<StudentEntry> getWaitlistedStudentsByClass(String semester, String courseCode) {
        connection = DBConnection.getConnection();
        allWaitlistedStudent = new ArrayList<StudentEntry>();

        try {
            String getAllScheduledStudentQuery = "SELECT studentid FROM APP.SCHEDULE Where semester = ? and Coursecode = ? and status ='Waitlist'";

            allWaitlistedStudentStatement = connection.prepareStatement(getAllScheduledStudentQuery);
            allWaitlistedStudentStatement.setString(1, semester);
            allWaitlistedStudentStatement.setString(2, courseCode);

            resultSet = allWaitlistedStudentStatement.executeQuery();

            while (resultSet.next()) {
                String studentid = resultSet.getString("studentid");
                String getDescQuery = "SELECT * FROM app.student WHERE studentid = ?";
                getStudentIDStatement = connection.prepareStatement(getDescQuery);
                getStudentIDStatement.setString(1, studentid);

                ResultSet studentIDResultSet = getStudentIDStatement.executeQuery();
                studentIDResultSet.next();

                StudentEntry rowStudentID = new StudentEntry(studentid, studentIDResultSet.getString("firstname"),
                        studentIDResultSet.getString("lastname"));
                allWaitlistedStudent.add(rowStudentID);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allWaitlistedStudent;
    }
}
