// FSM_tb.v
`timescale 1ns/1ps
module FSM_tb;
    reg clk, rst, din;
    wire found;

    FSM dut (.clk(clk), .rst(rst), .din(din), .found(found));

    // clock
    initial begin clk = 0; forever #5 clk = ~clk; end

    task feed_bit(input bit b);
    begin
        din = b;
        @(posedge clk); #1;
        $display("t=%0t din=%0d state_found=%0d", $time, din, found);
    end
    endtask

    integer i;
    reg [31:0] stream;
    integer    N;

    initial begin
        $dumpfile("fsm_tb.vcd");
        $dumpvars(0, FSM_tb);

        rst = 1; din = 0;
        repeat (2) @(posedge clk);
        rst = 0;

        // Example stream with overlaps: 1 0 1 1 0 1 1
        // matches at bits [0..3] and [3..6]
        reg [6:0] bits = 7'b1011011;
        for (i = 6; i >= 0; i = i - 1) begin
            feed_bit(bits[i]);
        end

        // Random-ish extra bits
        for (i = 0; i < 12; i = i + 1) begin
            feed_bit($random % 2);
        end

        $display("FSM TB done.");
        #10 $finish;
    end
endmodule
