from pyproj import Proj, transform # pip install pyproj
import csv

inProj = Proj(init='epsg:28992') # Amersfoort / RD New -- Netherlands - Holland - Dutch
outProj = Proj(init='epsg:4326') # WGS 84 -- WGS84 - World Geodetic System 1984, used in GPS
x1,y1 = 121234,487372 #espg:28992
x2,y2 = transform(inProj,outProj,x1,y1) # To epsg:4326
print(x2,y2)


# fron csv file

with open('save_lat_lon.csv', 'w', newline='') as save_lat_lon:
	fieldnames = ['dossier_number', 'file_number', 'x-coordinaat', 'y-coordinaat', 'lat', 'lon']
	writer = csv.DictWriter(save_lat_lon,fieldnames=fieldnames)
	writer.writeheader()
	with open('x_y.csv') as f:
		csv_reader = csv.reader(f,delimiter=';')
		headers = next(csv_reader, None)
		print(headers)
		print(csv_reader)
		for row in csv_reader:
			dossier_number =row[0]
			file_number = row[1]
			x = row[2]
			y = row[3]
			
			x1,y1 = x,y
			x2,y2 = transform(inProj,outProj,x1,y1)
			print(x2,y2)
			fields = [{'dossier_number': dossier_number
						,'file_number': file_number
						,'x-coordinaat': x
						,'y-coordinaat': y
						,'lat': x2
						,'lon': y2
						}]
			rows = fields
			writer.writerows(rows)