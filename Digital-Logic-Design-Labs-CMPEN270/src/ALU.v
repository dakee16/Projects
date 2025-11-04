// ALU.v
// Simple parameterized ALU with common ops.
// Ops (alu_op):
//  4'b0000 : ADD
//  4'b0001 : SUB
//  4'b0010 : AND
//  4'b0011 : OR
//  4'b0100 : XOR
//  4'b0101 : SLL (logical left)
//  4'b0110 : SRL (logical right)
//  4'b0111 : SRA (arith right)
//  4'b1000 : SLT  (signed  a < b)
//  4'b1001 : SLTU (unsigned a < b)

`timescale 1ns/1ps
module ALU #(
    parameter WIDTH = 32
)(
    input      [WIDTH-1:0] a,
    input      [WIDTH-1:0] b,
    input      [3:0]       alu_op,
    output reg [WIDTH-1:0] y,
    output                  zero,
    output reg              carry,
    output reg              overflow
);
    wire [WIDTH-1:0] b_neg = ~b + {{(WIDTH-1){1'b0}},1'b1}; // two's complement
    wire [WIDTH-1:0] sum_add;
    wire [WIDTH-1:0] sum_sub;
    wire             carry_add;
    wire             carry_sub;

    // Do add/sub in parallel so flags are easy
    assign {carry_add, sum_add} = {1'b0, a} + {1'b0, b};
    assign {carry_sub, sum_sub} = {1'b0, a} + {1'b0, b_neg};

    // Combinational ALU
    always @* begin
        y        = {WIDTH{1'b0}};
        carry    = 1'b0;
        overflow = 1'b0;

        case (alu_op)
            4'b0000: begin // ADD
                y        = sum_add;
                carry    = carry_add;
                overflow = (a[WIDTH-1] == b[WIDTH-1]) && (y[WIDTH-1] != a[WIDTH-1]);
            end
            4'b0001: begin // SUB  a - b
                y        = sum_sub;
                carry    = ~carry_sub; // "borrow" = ~carry_sub, carry flag here = !borrow
                overflow = (a[WIDTH-1] != b[WIDTH-1]) && (y[WIDTH-1] != a[WIDTH-1]);
            end
            4'b0010: y = a & b;                     // AND
            4'b0011: y = a | b;                     // OR
            4'b0100: y = a ^ b;                     // XOR
            4'b0101: y = a << b[$clog2(WIDTH)-1:0]; // SLL
            4'b0110: y = a >> b[$clog2(WIDTH)-1:0]; // SRL
            4'b0111: y = $signed(a) >>> b[$clog2(WIDTH)-1:0]; // SRA
            4'b1000: y = ($signed(a) < $signed(b)) ? {{(WIDTH-1){1'b0}},1'b1} : {WIDTH{1'b0}}; // SLT
            4'b1001: y = (a < b) ? {{(WIDTH-1){1'b0}},1'b1} : {WIDTH{1'b0}}; // SLTU
            default: y = {WIDTH{1'b0}};
        endcase
    end

    assign zero = (y == {WIDTH{1'b0}});

endmodule
