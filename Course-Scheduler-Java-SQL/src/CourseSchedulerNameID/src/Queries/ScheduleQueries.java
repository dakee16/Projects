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

import Entry.ScheduleEntry;
import Entry.StudentEntry;
import Main.DBConnection;

/**
 *
 * @author daksh
 */
public class ScheduleQueries {
    private static Connection connection = null;
    private static PreparedStatement addStudentStatement = null;
    private static PreparedStatement getScheduleByStudentStatement = null;
    private static PreparedStatement getScheduleStudentCountStatement = null;
    private static PreparedStatement allScheduledStudentClassStatement = null;
    private static PreparedStatement allWaitlistedStudentClassStatement = null;
    private static PreparedStatement deleteStudentStatement = null;
    private static PreparedStatement deleteScheduleStatement = null;
    private static PreparedStatement updateScheduleEntryStatement = null;

    private static ArrayList<ScheduleEntry> allScheduleList = new ArrayList<ScheduleEntry>();
    private static ArrayList<ScheduleEntry> allScheduleddStudentClass = new ArrayList<ScheduleEntry>();
    private static ArrayList<ScheduleEntry> allWaitlistedStudentClass = new ArrayList<ScheduleEntry>();
    private static ResultSet resultSet;

    public static void addScheduleEntry(ScheduleEntry entry) {
        connection = DBConnection.getConnection();

        try {
            String addScheduleQuery = "INSERT INTO app.schedule (Semester, CourseCode, StudentID, Status, Timestamp) VALUES (?, ?, ?, ?, ?)";
            addStudentStatement = connection.prepareStatement(addScheduleQuery);
            addStudentStatement.setString(1, entry.getSemester());
            addStudentStatement.setString(2, entry.getCourseCode());
            addStudentStatement.setString(3, entry.getStudentID());
            addStudentStatement.setString(4, entry.getStatus());
            addStudentStatement.setTimestamp(5, entry.getTimestamp());
            addStudentStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static ArrayList<ScheduleEntry> getScheduleByStudent(String semester, String studentID) {
        connection = DBConnection.getConnection();
        allScheduleList = new ArrayList<ScheduleEntry>();

        try {
            String getStudentScheduleQuery = "select * from app.schedule where semester = ? and studentid = ?";
            getScheduleByStudentStatement = connection.prepareStatement(getStudentScheduleQuery);
            getScheduleByStudentStatement.setString(1, semester);
            getScheduleByStudentStatement.setString(2, studentID);

            resultSet = getScheduleByStudentStatement.executeQuery();
            while (resultSet.next()) {
                ScheduleEntry rowScheduleEntry = new ScheduleEntry(semester, resultSet.getString("coursecode"),
                        studentID, resultSet.getString("status"), resultSet.getTimestamp("timestamp"));
                allScheduleList.add(rowScheduleEntry);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allScheduleList;
    }

    public static int getScheduledStudentCount(String currentSemester, String courseCode) {
        connection = DBConnection.getConnection();
        int studentCount = 0;

        try {
            String getStudentCountQuery = "select count(studentid) from app.schedule where semester = ? and courseCode = ? and status = 'Scheduled'";
            getScheduleStudentCountStatement = connection.prepareStatement(getStudentCountQuery);
            getScheduleStudentCountStatement.setString(1, currentSemester);
            getScheduleStudentCountStatement.setString(2, courseCode);

            resultSet = getScheduleStudentCountStatement.executeQuery();

            if (resultSet.next()) {
                studentCount = resultSet.getInt(1);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return studentCount;
    }

    public static ArrayList<ScheduleEntry> getScheduledStudentsByClass(String semester, String courseCode) {
        connection = DBConnection.getConnection();
        allScheduleddStudentClass = new ArrayList<ScheduleEntry>();

        try {
            String allWaitlistedStudentClassQuery = "SELECT * FROM APP.SCHEDULE Where semester = ? and coursecode = ? and status ='Scheduled' ORDER BY timestamp ASC ";

            allScheduledStudentClassStatement = connection.prepareStatement(allWaitlistedStudentClassQuery);
            allScheduledStudentClassStatement.setString(1, semester);
            allScheduledStudentClassStatement.setString(2, courseCode);
            resultSet = allScheduledStudentClassStatement.executeQuery();

            while (resultSet.next()) {
                ScheduleEntry rowScheduleEntry = new ScheduleEntry(semester, courseCode,
                        resultSet.getString("studentid"), resultSet.getString("status"),
                        resultSet.getTimestamp("timestamp"));
                allScheduleddStudentClass.add(rowScheduleEntry);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allScheduleddStudentClass;
    }

    public static ArrayList<ScheduleEntry> getWaitlistedStudentsByClass(String semester, String courseCode) {
        connection = DBConnection.getConnection();
        allWaitlistedStudentClass = new ArrayList<ScheduleEntry>();

        try {
            String allWaitlistedStudentClassQuery = "SELECT * FROM APP.SCHEDULE Where semester = ? and coursecode = ? and status ='Waitlist' ORDER BY timestamp ASC ";

            allWaitlistedStudentClassStatement = connection.prepareStatement(allWaitlistedStudentClassQuery);
            allWaitlistedStudentClassStatement.setString(1, semester);
            allWaitlistedStudentClassStatement.setString(2, courseCode);
            resultSet = allWaitlistedStudentClassStatement.executeQuery();

            while (resultSet.next()) {
                ScheduleEntry rowScheduleEntry = new ScheduleEntry(semester, courseCode,
                        resultSet.getString("studentid"), resultSet.getString("status"),
                        resultSet.getTimestamp("timestamp"));
                allWaitlistedStudentClass.add(rowScheduleEntry);
            }
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return allWaitlistedStudentClass;
    }

    public static Boolean isStudentWaitlisted(String semester, String studentID, String courseCode) {
        ArrayList<ScheduleEntry> waitlistedStudents = getWaitlistedStudentsByClass(semester, courseCode);
        for (ScheduleEntry scheduleEntry : waitlistedStudents) {
            if (scheduleEntry.getStudentID().equals(studentID)) {
                return true;
            }
        }
        return false;
    }

    public static void dropStudentScheduleByCourse(String semester, String studentID, String courseCode) {
        connection = DBConnection.getConnection();

        try {
            String deleteStudentScheduleQuery = "DELETE FROM APP.SCHEDULE WHERE studentid = ? and semester = ? and coursecode = ? ";
            deleteStudentStatement = connection.prepareStatement(deleteStudentScheduleQuery);
            deleteStudentStatement.setString(1, studentID);
            deleteStudentStatement.setString(2, semester);
            deleteStudentStatement.setString(3, courseCode);

            deleteStudentStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

    }

    public static void dropScheduleByCourse(String semester, String courseCode) {
        connection = DBConnection.getConnection();

        try {
            String deleteScheduleQuery = "DELETE FROM APP.SCHEDULE WHERE semester = ? and coursecode = ? ";
            deleteScheduleStatement = connection.prepareStatement(deleteScheduleQuery);
            deleteScheduleStatement.setString(1, semester);
            deleteScheduleStatement.setString(2, courseCode);

            deleteScheduleStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

    public static void updateScheduleEntry(ScheduleEntry entry) {
        connection = DBConnection.getConnection();

        try {
            String updateScheduleEntryQuery = "UPDATE APP.SCHEDULE SET status = 'Scheduled' WHERE studentid = ? and coursecode = ?";
            updateScheduleEntryStatement = connection.prepareStatement(updateScheduleEntryQuery);
            updateScheduleEntryStatement.setString(1, entry.getStudentID());
            updateScheduleEntryStatement.setString(2, entry.getCourseCode());

            updateScheduleEntryStatement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }
    }

}
