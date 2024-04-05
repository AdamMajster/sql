CREATE TABLE dni_tygodnia (
    id_dnia  INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nazwa_dnia VARCHAR(20) NOT NULL,
    nazwa_skr_dnia VARCHAR(5) NOT NULL
);



INSERT INTO dni_tygodnia (id_dnia, nazwa_dnia, nazwa_skr_dnia) VALUES
('Poniedziałek', 'Poniedziałek', 'Pon'),
('Wtorek', 'Wtorek', 'Wto'),
('Środa', 'Środa', 'Śro'),
('Czwartek', 'Czwartek', 'Czw'),
('Piątek', 'Piątek', 'Pią'),
('Sobota', 'Sobota', 'Sob'),
('Niedziela', 'Niedziela',  'Nie')
;