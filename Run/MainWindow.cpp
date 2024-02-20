#include "MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QWidget(parent) {
    setWindowTitle("GD Bot");

    setStyleSheet("background-color: #333; color: white;");

    runButton = new QPushButton("Run Bot", this);
    runButton->setStyleSheet("background-color: #ff3333; color: white;");

    stopButton = new QPushButton("Stop Bot", this);
    stopButton->setStyleSheet("background-color: #ff3333; color: white;");

    botProcess = new QProcess(this);

    connect(runButton, &QPushButton::clicked, this, &MainWindow::runBot);
    connect(stopButton, &QPushButton::clicked, this, &MainWindow::stopBot);

    QVBoxLayout *layout = new QVBoxLayout(this);
    layout->addWidget(runButton);
    layout->addWidget(stopButton);

    setLayout(layout);
}

void MainWindow::runBot() {
    QString filePath = QCoreApplication::applicationDirPath() + "/GDBOT/app.py";
    botProcess->start("python", QStringList() << filePath);
}

void MainWindow::stopBot() {
    botProcess->close();
}
