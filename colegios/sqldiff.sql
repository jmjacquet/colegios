BEGIN;
-- Application: colegio
-- Model: Cuota
ALTER TABLE `cuota_web`
	MODIFY `importe_base` numeric(15, 2);
ALTER TABLE `cuota_web`
	MODIFY `importe_base_2` numeric(15, 2);
ALTER TABLE `cuota_web`
	MODIFY `saldo` numeric(15, 2);
-- Model: Configuracion
ALTER TABLE `configuracion`
	MODIFY `varios1` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `punitorios` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `tipo_punitorios` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `linea1` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `linea2` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `link_retorno` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `mantenimiento` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `ncuerpo1` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `ncuerpo2` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `ncuerpo3` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `codigo_visible` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `alicuota_unidad` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `alicuota_coeficiente` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `detalleContrib` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `liquidacion_web` DROP NOT NULL;
ALTER TABLE `configuracion`
	MODIFY `email` DROP NOT NULL;
-- Model: Sinc
-- Table missing: sinc
COMMIT;
