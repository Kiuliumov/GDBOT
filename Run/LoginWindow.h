#ifndef LOGINWINDOW_H
#define LOGINWINDOW_H

#include <QWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>
#include <QJsonObject>

class LoginWindow : public QWidget {
    Q_OBJECT

public:
    LoginWindow(QWidget *parent = nullptr);

private slots:
    void attemptLogin();

private:
    QLineEdit *usernameEdit;
    QLineEdit *passwordEdit;
    QPushButton *loginButton;
    QJsonObject users;
};

#endif // LOGINWINDOW_H
