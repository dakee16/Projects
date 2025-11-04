// ALU_tb.v
`timescale 1ns/1ps
module ALU_tb;
    localparam W = 32;

    reg  [W-1:0] a, b;
    reg  [3:0]   op;
    wire [W-1:0] y;
    wire         z;
    wire         c;
    wire         ov;

    ALU #(.WIDTH(W)) dut (
        .a(a), .b(b), .alu_op(op),
        .y(y), .zero(z), .carry(c), .overflow(ov)
    );

    task run_case(input [3:0] t_op, input [W-1:0] ta, input [W-1:0] tb, input [W-1:0] expect);
    begin
        op = t_op; a = ta; b = tb; #1;
        $display("op=%b a=%0d b=%0d -> y=%0d z=%0d c=%0d ov=%0d (expect %0d)",
                  op, $signed(a), $signed(b), $signed(y), z, c, ov, $signed(expect));
    end
    endtask

    initial begin
        $dumpfile("alu_tb.vcd");
        $dumpvars(0, ALU_tb);

        // ADD
        run_case(4'b0000, 32'd10, 32'd5, 32'd15);
        // SUB
        run_case(4'b0001, 32'd10, 32'd5, 32'd5);
        // AND/OR/XOR
        run_case(4'b0010, 32'hF0F0, 32'h0FF0, 32'h00F0);
        run_case(4'b0011, 32'hF0F0, 32'h0FF0, 32'hFFF0);
        run_case(4'b0100, 32'hAAAA, 32'h0F0F, 32'hA5A5);
        // Shifts
        run_case(4'b0101, 32'd1, 32'd4, 32'd16);
        run_case(4'b0110, 32'd16, 32'd2, 32'd4);
        // SRA with negative
        op = 4'b0111; a = -32'sd8; b = 32'd1; #1; $display("SRA y=%0d", $signed(y));
        // SLT signed & SLTU
        op = 4'b1000; a = -32'sd1; b = 32'sd1; #1; $display("SLT(-1<1) y=%0d", y);
        op = 4'b1001; a = 32'hFFFFFFFF; b = 32'd1; #1; $display("SLTU(0xFFFF.. < 1) y=%0d", y);

        $display("ALU TB done.");
        #5 $finish;
    end
endmodule
