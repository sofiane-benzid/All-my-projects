for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            int rank = 0;
            while (candidates[preferences[i][rank]].eliminated == true)
                rank++;

            if (preferences[i][rank] == j)
            {
                candidates[j].votes ++;
            }
        }
    }