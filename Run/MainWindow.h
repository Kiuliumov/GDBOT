#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QProcess>

class MainWindow : public QWidget {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);

private slots:
    void runBot();
    void stopBot();

private:
    QPushButton *runButton;
    QPushButton *stopButton;
    QProcess *botProcess;
};

#endif // MAINWINDOW_H
