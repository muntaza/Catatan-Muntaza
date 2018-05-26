DROP VIEW IF EXISTS view_sppd CASCADE;


CREATE VIEW view_sppd AS


SELECT
pegawai.nama_pegawai,
pegawai.nip,
pegawai.pangkat,

skpd.nama_skpd,

sppd.no_sppd,
sppd.tanggal_berangkat,
sppd.tanggal_kembali,
sppd.keterangan



FROM
pegawai join sppd on pegawai.id = sppd.id_pegawai
join skpd on skpd.id = pegawai.id_skpd

WHERE
1 = 1

;


GRANT ALL PRIVILEGES ON view_sppd TO kalender;
REVOKE INSERT, UPDATE, DELETE ON view_sppd FROM kalender;
