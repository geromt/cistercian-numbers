# Makefile to generate several svg sample images with the CLI

cli := python3 ../app/cistercian_cli.py
dir := ./samples

all: clean init generate

init:
	mkdir $(dir)

generate:
	$(cli) 0 -f $(dir)/0.svg
	$(cli) 1111 -f $(dir)/1111.svg
	$(cli) 2222 -f $(dir)/2222.svg
	$(cli) 3333 -f $(dir)/3333.svg
	$(cli) 4444 -f $(dir)/4444.svg
	$(cli) 5555 -f $(dir)/5555.svg
	$(cli) 6666 -f $(dir)/6666.svg
	$(cli) 7777 -f $(dir)/7777.svg
	$(cli) 8888 -f $(dir)/8888.svg
	$(cli) 9999 -f $(dir)/9999.svg
	$(cli) 9 -f $(dir)/9.svg
	$(cli) 90 -f $(dir)/90.svg
	$(cli) 900 -f $(dir)/900.svg
	$(cli) 9000 -f $(dir)/9000.svg
	$(cli) 1234 -f $(dir)/1234.svg
	$(cli) 5678 -f $(dir)/5678.svg
	$(cli) 1234 -f $(dir)/1234_size.svg --width 720 --height 480
	$(cli) 5678 -f $(dir)/5678_size.svg --width 720 --height 480
	$(cli) 1234 -f $(dir)/1234_size2.svg --width 1440 --height 480
	$(cli) 5678 -f $(dir)/5678_size2.svg --width 1440 --height 480
	$(cli) 1234 -f $(dir)/1234_color.svg --background "#A82810" --color "#FBC490"
	$(cli) 5678 -f $(dir)/5678_color.svg --background "#A82810" --color "#FBC490"
	$(cli) 1234 -f $(dir)/1234_line.svg --stroke 50
	$(cli) 5678 -f $(dir)/5678_line.svg --stroke 50

clean:
	rm -rf $(dir)
