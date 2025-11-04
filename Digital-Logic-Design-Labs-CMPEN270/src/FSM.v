// FSM.v
// Moore FSM that asserts 'found' for one cycle when it detects the bit sequence 1011.
// Overlapping sequences supported (e.g., 10111 contains two matches).

`timescale 1ns/1ps
module FSM (
    input  clk,
    input  rst,   // synchronous, active-high
    input  din,   // serial input bit
    output reg found // 1 when pattern 1011 detected
);
    typedef enum reg [2:0] {
        S0   = 3'd0, // no match
        S1   = 3'd1, // seen '1'
        S10  = 3'd2, // seen '10'
        S101 = 3'd3, // seen '101'
        S1011= 3'd4  // seen '1011' (Moore output state)
    } state_t;

    state_t state, next;

    // Next-state logic
    always @* begin
        next = state;
        case (state)
            S0:    next = din ? S1   : S0;
            S1:    next = din ? S1   : S10;
            S10:   next = din ? S101 : S0;
            S101:  next = din ? S1011: S10;
            S1011: next = din ? S1   : S10; // allow overlap
            default: next = S0;
        endcase
    end

    // State register
    always @(posedge clk) begin
        if (rst) state <= S0;
        else     state <= next;
    end

    // Moore output: only high in S1011
    always @* begin
        found = (state == S1011);
    end

endmodule
