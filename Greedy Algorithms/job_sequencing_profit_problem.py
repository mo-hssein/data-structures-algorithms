import unittest


def job_sequencing_profit(jobs, profits, deadlines):
    """
    Schedule jobs to maximize profit given their profits and deadlines.

    Args:
    - jobs (List[str]): List of job names.
    - profits (List[int]): List of profits corresponding to each job.
    - deadlines (List[int]): List of deadlines corresponding to each job.

    Returns:
    - List[str], int: A tuple containing the list of scheduled jobs and the total profit.
    """
    if len(jobs) < 1:
        return [], 0

    n = len(jobs)

    # A list that collects the job name, deadline, and profit.
    list_of_jobs = [(jobs[i], profits[i], deadlines[i]) for i in range(n)]

    # Sort the list based on profit, Use lambda to access the profit index in tuple.
    list_of_jobs.sort(key=lambda x: x[1], reverse=True)

    # A list to reveal when the job deadline is finished or not by False or true.
    selected_jobs = [False] * (max(deadlines) + 1)

    # List to store completed jobs by deadline
    job_sequence = [""] * (max(deadlines) + 1)

    # A variable to store the final profit
    total_profit = 0

    for i in range(n):
        deadline = list_of_jobs[i][2]
        while deadline > 0 and selected_jobs[deadline]:
            deadline -= 1

        if deadline > 0:
            selected_jobs[deadline] = True
            job_sequence[deadline] = list_of_jobs[i][0]
            total_profit += list_of_jobs[i][1]

    job_sequence.pop(0)
    return job_sequence, total_profit


# unit testing

#      |
#      |
#      V


class TestJobSequencingProblem(unittest.TestCase):

    def test_job_sequencing_profit(self):
        jobs1 = ["A", "B", "C", "D", "E"]
        deadlines1 = [1, 1, 1, 1, 1]
        profits1 = [100, 90, 80, 70, 60]
        result1 = job_sequencing_profit(jobs1, profits1, deadlines1)
        self.assertEqual(result1, (["A"], 100))

        jobs2 = []
        deadlines2 = []
        profits2 = []
        result2 = job_sequencing_profit(jobs2, profits2, deadlines2)
        self.assertEqual(result2, ([], 0))

        jobs3 = ["A", "B", "C"]
        deadlines3 = [2, 2, 2]
        profits3 = [50, 30, 40]
        result3 = job_sequencing_profit(jobs3, profits3, deadlines3)
        self.assertEqual(result3, (["C", "A"], 90))

        jobs4 = ["A", "B", "C", "D", "E"]
        deadlines4 = [2, 2, 1, 1, 3]
        profits4 = [100, 30, 80, 70, 60]
        result4 = job_sequencing_profit(jobs4, profits4, deadlines4)
        self.assertEqual(result4, (["C", "A", "E"], 240))

        jobs5 = ["A"]
        deadlines5 = [1]
        profits5 = [100]
        result5 = job_sequencing_profit(jobs5, profits5, deadlines5)
        self.assertEqual(result5, (["A"], 100))

        jobs6 = ["A", "A", "B", "B", "C"]
        deadlines6 = [2, 2, 2, 2, 2]
        profits6 = [50, 30, 40, 20, 60]
        result6 = job_sequencing_profit(jobs6, profits6, deadlines6)
        self.assertEqual(result6, (["A", "C"], 110))


if __name__ == "__main__":
    unittest.main()
