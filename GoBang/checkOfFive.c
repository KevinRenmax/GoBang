int check_of_five(int(*balls)[11],const int hor,const int col,int &score)
{
	const int max = 5;	//判断五个连成横、竖、对角线一排
	int i, j, x, y, search;	
	score = 0;

	for (i = 1; i <= hor; i++) {	//判断横向是否连成五个
		search = 1;
		for (j = 2; j <= col+1; j++)
			if (balls[i][j - 1] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j - 1, y = i; search > 0;x--, search--)
						balls[y][x] = 0;
				}
				else
					search = 1;
	}

	for (j = 1; j <= col; j++) {	//判断纵向是否连成五个
		search = 1;
		for (i = 2; i <= hor+1; i++)
			if (balls[i - 1][j] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j, y = i - 1; search > 0; y--, search--) 
						balls[y][x] = 0;
				}
				else
					search = 1;
	}

	int m;
	for (m = 4; m < col; m++) {	//判断主对角线方向所有斜线是否连成5个
		search = 1;
		for (j = col - m + 1, i = 2; j <= col+1; i++, j++)
			if (balls[i - 1][j - 1] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j - 1, y = i - 1; search > 0; x--, y--, search--)
						balls[y][x] = 0;
				}
				else
					search = 1;
	}
	for (m = 4; m < hor; m++){	//判断副对角线方向所有斜线是否连成5个
		search=1;
		for (i = hor - m + 1, j = 2; i <= hor + 1; i++, j++)
			if (balls[i - 1][j - 1] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j - 1, y = i - 1; search > 0; x--, y--, search--)
						balls[y][x] = 0;
				}
				else
					search = 1;
	}
	for (m = 5; m <=col; m++) {
		search = 1;
		for (i = 2, j = m-1; j >= 0; i++, j--)
			if (balls[i - 1][j + 1] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j + 1, y = i - 1; search > 0; x++, y--, search--)
						balls[y][x] = 0;
				}
				else
					search = 1;
	}
	for (m = 4; m <= hor; m++) {
		search = 1;
		for (j = col-m+1, i = hor - 1; j <= col+1; i--, j++)
			if (balls[i + 1][j - 1] == balls[i][j] && balls[i][j])
				search++;
			else
				if (search >= max) {
					score += search;
					for (x = j - 1, y = i + 1; search > 0; x--, y++, search--)
						balls[y][x] = 0;
				}
				else
					search = 1;
	}
	if (score >= max)	//如果五个连在一起则返回1，否则返回0
		return 1;
	else
		return 0;
}

