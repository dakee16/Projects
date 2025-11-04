/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Entry;

/**
 *
 * @author daksh
 */
public class ClassDescription {
    private String courseCode;
    private String description;
    private int seats;

    public ClassDescription(String courseCode, String description, int seats) {
        this.courseCode = courseCode;
        this.description = description;
        this.seats = seats;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getCourseDescription() {
        return description;
    }

    public int getSeats() {
        return seats;
    }
}