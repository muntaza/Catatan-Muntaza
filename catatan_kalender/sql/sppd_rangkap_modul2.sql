DROP VIEW IF EXISTS view_sppd_rangkap_modul2 CASCADE;


CREATE VIEW view_sppd_rangkap_modul2 AS


SELECT

nama_pegawai,
nip,
pangkat,

nama_skpd,

no_sppd,
tanggal_berangkat,
tanggal_kembali,
id_pegawai,
id_skpd,
keterangan,

tanggal_berangkat_sebelum,
tanggal_kembali_sebelum,

tanggal_berangkat_sesudah,
tanggal_kembali_sesudah,

rank

FROM

view_sppd_rangkap


WHERE
1 = 1


ORDER BY id_pegawai, rank

;


GRANT ALL PRIVILEGES ON view_sppd_rangkap_modul2 TO kalender;
REVOKE INSERT, UPDATE, DELETE ON view_sppd_rangkap_modul2 FROM kalender;

GRANT ALL PRIVILEGES ON pegawai,sppd TO kalender;
