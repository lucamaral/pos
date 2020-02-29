-- 1

-- Alunos matriculados ativos

select aluno_id, a.nome from alunos_campus.matricula m
join alunos_campus.aluno a on (m.aluno_id = a.id)
where m.data_trancamento is null or m.data_trancamento > now()
group by aluno_id, a.nome;

-- 2

-- Alunos em aula no campus em determinado horario

select a.nome, m.data_trancamento from alunos_campus.presenca p
join alunos_campus.aluno a on (p.aluno_id = a.id)
join alunos_campus.grade g on (g.hora_inicial < now() and g.hora_final > now())
join alunos_campus.disciplina d on (g.disciplina_id = d.id)
join alunos_campus.matricula m on (m.disciplina_id = d.id and m.aluno_id = a.id)
where
      p.data_hora_entrada < now() and
      p.data_hora_saida is null;

-- 3

-- Professores ministrando as disciplinas

select p.nome, d.descricao from alunos_campus.professor p
join alunos_campus.disciplina d on (d.professor_id = p.id);

-- Professores ministrando as disciplinas em determinado horario

select p.nome, d.descricao from alunos_campus.professor p
join alunos_campus.disciplina d on (d.professor_id = p.id)
join alunos_campus.grade g on (d.id = g.disciplina_id)
where g.hora_inicial < now() and g.hora_final > now();