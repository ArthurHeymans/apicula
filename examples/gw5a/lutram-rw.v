// RAM16SDP4 in shadow SRAM checked against a flip-flop model, with
// different data per bit, a gated write enable and non-zero initial
// contents. The LEDs count while the RAM matches the model and stop at
// the first mismatch.
module top(input clk, input key_i, output [`LEDS_NR-1:0] led);
	reg [7:0] cnt = 0;
	wire [3:0] wad = cnt[3:0], rad = cnt[3:0] - 4'd1;
	wire wre = cnt[5];
	wire [3:0] di = {key_i, ~key_i, cnt[6], cnt[7] ^ key_i};
	localparam [15:0] I0 = 16'hA5C3, I1 = 16'h0F0F, I2 = 16'h3333, I3 = 16'h5555;
	wire [3:0] dout;
	RAM16SDP4 #(.INIT_0(I0), .INIT_1(I1), .INIT_2(I2), .INIT_3(I3)) ram (
		.DI(di), .WAD(wad), .RAD(rad), .WRE(wre), .CLK(clk), .DO(dout));

	reg [3:0] model [0:15];
	integer i;
	initial for (i = 0; i < 16; i = i + 1)
		model[i] = {I3[i], I2[i], I1[i], I0[i]};

	reg bad = 0;
	always @(posedge clk) begin
		cnt <= cnt + 1'b1;
		if (wre)
			model[wad] <= di;
		if (dout != model[rad])
			bad <= 1;
	end

	reg [25:0] ctr = 0;
	always @(posedge clk)
		if (!bad)
			ctr <= ctr + 1'b1;
	assign led = ctr[25 -: `LEDS_NR];
endmodule
