	void insertion_sort()
	{
		for (int i = 1; i < n; ++i)
		{
			int k = i;
			int tmp;
			while (v[k] < v[k - 1] && k>0)
			{
				tmp = v[k];
				v[k] = v[k - 1];
				v[k - 1] = tmp;
				--k;
			}
		}
		return;
	}