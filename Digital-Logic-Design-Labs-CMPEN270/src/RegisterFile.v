// RegisterFile.v
// Two read ports, one write port register file.
// Asynchronous reads, synchronous write on rising edge.
// R0 hard-wired to 0 (optional RISC-V style).

`timescale 1ns/1ps
module RegisterFile #(
    parameter WIDTH = 32,
    parameter DEPTH = 32,
    parameter ADDR_W = $clog2(DEPTH)
)(
    input                   clk,
    input                   rst,        // active-high synchronous reset
    input                   we,         // write enable
    input      [ADDR_W-1:0] waddr,
    input      [WIDTH-1:0]  wdata,
    input      [ADDR_W-1:0] raddr1,
    input      [ADDR_W-1:0] raddr2,
    output     [WIDTH-1:0]  rdata1,
    output     [WIDTH-1:0]  rdata2
);

    reg [WIDTH-1:0] mem [0:DEPTH-1];
    integer i;

    // synchronous write + reset
    always @(posedge clk) begin
        if (rst) begin
            for (i = 0; i < DEPTH; i = i + 1) begin
                mem[i] <= {WIDTH{1'b0}};
            end
        end else if (we && (waddr != {ADDR_W{1'b0}})) begin
            mem[waddr] <= wdata;
        end
        // keep x0 hardwired to 0
        mem[0] <= {WIDTH{1'b0}};
    end

    // asynchronous read
    assign rdata1 = (raddr1 == {ADDR_W{1'b0}}) ? {WIDTH{1'b0}} : mem[raddr1];
    assign rdata2 = (raddr2 == {ADDR_W{1'b0}}) ? {WIDTH{1'b0}} : mem[raddr2];

endmodule
