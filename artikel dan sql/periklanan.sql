-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Nov 2025 pada 12.23
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `periklanan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `advertiser`
--

CREATE TABLE `advertiser` (
  `kd_advertiser` int(11) NOT NULL,
  `nama_advertiser` varchar(100) DEFAULT NULL,
  `pemberi_order` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `kota` varchar(50) DEFAULT NULL,
  `kodepos` varchar(10) DEFAULT NULL,
  `no_telp` varchar(15) DEFAULT NULL,
  `no_fax` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `advertiser`
--

INSERT INTO `advertiser` (`kd_advertiser`, `nama_advertiser`, `pemberi_order`, `alamat`, `kota`, `kodepos`, `no_telp`, `no_fax`, `email`) VALUES
(1, 'Azril Nazar', 'Pasha Andhika', 'Sungai Lulut', 'Banjarmasin', '2322', '081250440142', '1144', 'raendraaa@gmail.com');

-- --------------------------------------------------------

--
-- Struktur dari tabel `biaya_iklan`
--

CREATE TABLE `biaya_iklan` (
  `no_invoice` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `kd_advertiser` int(11) DEFAULT NULL,
  `kd_iklan` int(11) DEFAULT NULL,
  `frekwensi` int(11) DEFAULT NULL,
  `jumlah_bayar` decimal(12,2) DEFAULT NULL,
  `pph` decimal(12,2) DEFAULT NULL,
  `total_bayar` decimal(12,2) DEFAULT NULL,
  `terbilang` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `biaya_iklan`
--

INSERT INTO `biaya_iklan` (`no_invoice`, `tanggal`, `kd_advertiser`, `kd_iklan`, `frekwensi`, `jumlah_bayar`, `pph`, `total_bayar`, `terbilang`) VALUES
(12345, '2025-11-11', 1, 1, 12345, 23.00, 5.00, 18.00, 'Delapan Belas Rupiah');

-- --------------------------------------------------------

--
-- Struktur dari tabel `iklan`
--

CREATE TABLE `iklan` (
  `kd_iklan` int(11) NOT NULL,
  `produk` varchar(100) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `versi` varchar(50) DEFAULT NULL,
  `durasi` int(11) DEFAULT NULL,
  `jenis` varchar(50) DEFAULT NULL,
  `harga` decimal(12,2) DEFAULT NULL,
  `kd_advertiser` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `iklan`
--

INSERT INTO `iklan` (`kd_iklan`, `produk`, `brand`, `versi`, `durasi`, `jenis`, `harga`, `kd_advertiser`) VALUES
(1, 'Shampoo', 'Zink', '1', 12000, 'cair', 10000.00, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyiaran`
--

CREATE TABLE `penyiaran` (
  `id_siar` int(11) NOT NULL,
  `kd_iklan` int(11) DEFAULT NULL,
  `produk` varchar(100) DEFAULT NULL,
  `periode` varchar(50) DEFAULT NULL,
  `air_time` varchar(50) DEFAULT NULL,
  `tgl_mulai` varchar(2) DEFAULT NULL,
  `tgl_selesai` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penyiaran`
--

INSERT INTO `penyiaran` (`id_siar`, `kd_iklan`, `produk`, `periode`, `air_time`, `tgl_mulai`, `tgl_selesai`) VALUES
(1, 1, '1', 'hehe', 'huhu', '01', '12');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `advertiser`
--
ALTER TABLE `advertiser`
  ADD PRIMARY KEY (`kd_advertiser`);

--
-- Indeks untuk tabel `biaya_iklan`
--
ALTER TABLE `biaya_iklan`
  ADD PRIMARY KEY (`no_invoice`),
  ADD KEY `kd_advertiser` (`kd_advertiser`),
  ADD KEY `kd_iklan` (`kd_iklan`);

--
-- Indeks untuk tabel `iklan`
--
ALTER TABLE `iklan`
  ADD PRIMARY KEY (`kd_iklan`),
  ADD KEY `kd_advertiser` (`kd_advertiser`);

--
-- Indeks untuk tabel `penyiaran`
--
ALTER TABLE `penyiaran`
  ADD PRIMARY KEY (`id_siar`),
  ADD KEY `kd_iklan` (`kd_iklan`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `advertiser`
--
ALTER TABLE `advertiser`
  MODIFY `kd_advertiser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `biaya_iklan`
--
ALTER TABLE `biaya_iklan`
  MODIFY `no_invoice` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12346;

--
-- AUTO_INCREMENT untuk tabel `iklan`
--
ALTER TABLE `iklan`
  MODIFY `kd_iklan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `penyiaran`
--
ALTER TABLE `penyiaran`
  MODIFY `id_siar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `biaya_iklan`
--
ALTER TABLE `biaya_iklan`
  ADD CONSTRAINT `biaya_iklan_ibfk_1` FOREIGN KEY (`kd_advertiser`) REFERENCES `advertiser` (`kd_advertiser`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `biaya_iklan_ibfk_2` FOREIGN KEY (`kd_iklan`) REFERENCES `iklan` (`kd_iklan`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `iklan`
--
ALTER TABLE `iklan`
  ADD CONSTRAINT `iklan_ibfk_1` FOREIGN KEY (`kd_advertiser`) REFERENCES `advertiser` (`kd_advertiser`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `penyiaran`
--
ALTER TABLE `penyiaran`
  ADD CONSTRAINT `penyiaran_ibfk_1` FOREIGN KEY (`kd_iklan`) REFERENCES `iklan` (`kd_iklan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
