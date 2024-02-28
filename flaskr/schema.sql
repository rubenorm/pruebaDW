DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS vehiculo;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE vehiculo (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dueno INTEGER NOT NULL,
  placas TEXT NOT NULL,
  lat FLOAT NOT NULL,
  lon FLOAT NOT NULL,
  FOREIGN KEY (dueno) REFERENCES user (id)
);

INSERT INTO user (username, password) VALUES
  ("Ruben", "abc123"),
  ("Jose", "bcd456"),
  ("Juan", "efg789");

INSERT INTO vehiculo (dueno, placas, lat, lon) VALUES
  (1, "ASD563", 125.35, -245.35),
  (2, "LD-35H", 46.476, -2.346),
  (1, "SGR-36-F", 26.3, 35.73),
  (2, "SDF-H35", 123, -2.76),
  (3, "THD-36E", 125.35, -245.35);
	
