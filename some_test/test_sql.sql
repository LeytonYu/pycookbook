SELECT
	question_id,
	count(question_id) AS ctt
FROM
	`t_Q&A_questionlog` tlog
LEFT JOIN `t_Q&A_questions` tque ON tlog.question_id = tque.id
WHERE
	`create_time` BETWEEN '2021-06-14 14:52:55'
AND '2021-06-20 23:53:04'
GROUP BY
	question_id
ORDER BY
	ctt DESC
LIMIT 0,10