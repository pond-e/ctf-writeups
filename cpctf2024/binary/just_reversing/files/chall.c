#include <stdio.h>
#include <string.h>

int main() {
	char flag_enc[30] = "";
	char flag[30];
	FILE *f;
	f = fopen("flag.txt", "r");
	if (f == NULL) {
		printf("flag.txt not found\n");
		return 1;
	}
	fscanf(f, "%s", flag);
	fclose(f);

	for (int i = 0; i < strlen(flag); i++) {
		char chr = flag[i];
		flag_enc[strlen(flag) - i - 1] = chr / 16 + chr % 16 * 16;
	}

	f = fopen("flag_enc.txt", "w");
	fprintf(f, "%s", flag_enc);
	fclose(f);

	return 0;
}
