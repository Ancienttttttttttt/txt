import socket

new_socket = socket.socket()#создание сокета
new_socket.bind(("127.0.0.1", 50))#вводим ip-адрес localhost и порт по которому можно подключиться к серверу
new_socket.listen()#запуск сервера

print("Сервер запущен!")
name = input("Введите свое имя:")
conn, add = new_socket.accept()#регистрация клиента

client = (conn.recv(1024).decode())
print(client + ' присоединился!')
conn.send(name.encode())

while True:#цикл для писания сообщений, его декодирования и вывода на экран
    message = input('Я: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
