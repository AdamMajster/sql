CREATE TABLE dni_tygodnia (
    id_dnia  INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nazwa_skr_dnia VARCHAR(5) NOT NULL
);

INSERT INTO dni_tygodnia (id_dnia, nazwa_skr_dnia) VALUES
('Poniedziałek', 'Pon'),
('Wtorek', 'Wto'),
('Środa', 'Śro'),
('Czwartek', 'Czw'),
('Piątek', 'Pią'),
('Sobota', 'Sob'),
('Niedziela', 'Nie')
;