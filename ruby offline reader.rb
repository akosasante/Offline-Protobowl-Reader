include "mysql"

begin
	dbh = mysql.real_connect("localhost", "root", "island", "quizbowl")
	puts "successful connection to " + dbh.get_server_info
rescue mysql::Error => e
	puts "Error code: #{e.errno}"
	puts "Error message: #{e.error}"
	puts "Error SQLSTATE: #{e.sqlstate}" if e.respond_to? ("sqlstate")
ensure
	dbh.close if dbh
end

