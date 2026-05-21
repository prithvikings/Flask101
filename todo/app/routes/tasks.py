from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp=Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        flash('Please log in to view tasks.', 'warning')
        return redirect(url_for('auth.login'))

    tasks=Task.query.all()
    return render_template('tasks.html', tasks=tasks)


@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        flash('Please log in to add tasks.', 'warning')
        return redirect(url_for('auth.login'))

    title=request.form['title']
    if title:
        new_task=Task(title=title, status='pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task=Task.query.get(task_id)
    if task:
        if task.status=='Pending':
            task.status='Working'
        elif task.status=='Working':
            task.status='Completed'
        else:
            task.status='Pending'
        db.session.commit()
        flash('Task updated successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task=Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared successfully!', 'info')
    return redirect(url_for('tasks.view_tasks'))

