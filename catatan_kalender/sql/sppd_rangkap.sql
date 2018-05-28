DROP VIEW IF EXISTS view_sppd_rangkap CASCADE;


CREATE VIEW view_sppd_rangkap AS


SELECT

pegawai.nama_pegawai,
pegawai.nip,
pegawai.pangkat,

skpd.nama_skpd,

sppd.no_sppd,
sppd.tanggal_berangkat,
sppd.tanggal_kembali,
sppd.id_pegawai,
sppd.id_skpd,
sppd.keterangan


FROM
pegawai join sppd on pegawai.id = sppd.id_pegawai
join skpd on skpd.id = pegawai.id_skpd

WHERE
1 = 1

;


GRANT ALL PRIVILEGES ON view_sppd_rangkap TO kalender;
REVOKE INSERT, UPDATE, DELETE ON view_sppd_rangkap FROM kalender;

GRANT ALL PRIVILEGES ON pegawai,sppd TO kalender;
REVOKE INSERT, UPDATE, DELETE ON pegawai,sppd FROM kalender;

