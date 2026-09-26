// Registers in IO logic: built with ireg_in_iob and oreg_in_iob, the key
// is sampled by an input register and the LEDs are driven by output
// registers with clock enable and synchronous reset.
module top (
	input clk,
	input key_i,
	input rst_i,
	output [`LEDS_NR-1:0] led
);

reg key_q;
always @(posedge clk) begin
	key_q <= key_i;
end
wire key = key_q ^ `INV_BTN;

reg [25:0] ctr_q;
always @(posedge clk) begin
	ctr_q <= ctr_q + 1'b1;
end

reg [`LEDS_NR-1:0] led_q;
always @(posedge clk) begin
	if (rst_i) begin
		led_q <= 0;
	end else if (key) begin
		led_q <= ctr_q[25 -: `LEDS_NR];
	end
end
assign led = led_q;

endmodule
