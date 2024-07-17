NYSE_tickers = [
    'A', 'AA', 'AAC', 'AAN', 'AAP', 'AAT', 'AB', 'ABB', 'ABBV', 'ABC', 'ABEV', 'ABG', 'ABM', 'ABR', 'ABT', 'AC', 
    'ACA', 'ACC', 'ACCO', 'ACEL', 'ACH', 'ACI', 'ACM', 'ACN', 'ACP', 'ACRE', 'ACV', 'ADC', 'ADM', 'ADNT', 'ADS', 
    'ADT', 'AEE', 'AEG', 'AEL', 'AEM', 'AEO', 'AEP', 'AES', 'AFL', 'AFRM', 'AG', 'AGCO', 'AGD', 'AGI', 'AGL', 
    'AGO', 'AGR', 'AGRO', 'AGS', 'AGX', 'AHH', 'AHL', 'AHT', 'AI', 'AIG', 'AIMC', 'AIN', 'AIR', 'AIT', 'AIV', 
    'AIZ', 'AJG', 'AJRD', 'AJX', 'AKO', 'AKR', 'AL', 'ALB', 'ALC', 'ALE', 'ALEX', 'ALG', 'ALGM', 'ALK', 'ALL', 
    'ALLE', 'ALLY', 'ALSN', 'ALTG', 'ALV', 'ALX', 'AM', 'AMBC', 'AMCR', 'AME', 'AMG', 'AMH', 'AMK', 'AMN', 'AMP', 
    'AMRC', 'AMRX', 'AMT', 'AMX', 'AN', 'ANET', 'ANF', 'ANH', 'ANTM', 'AOD', 'AON', 'AOS', 'AP', 'APAM', 'APD', 
    'APG', 'APHA', 'APLE', 'APO', 'APTS', 'APTV', 'APY', 'AQN', 'AQUA', 'AR', 'ARA', 'ARCO', 'ARC', 'ARCH', 'ARCO', 
    'ARDC', 'ARE', 'ARES', 'ARI', 'ARL', 'ARLO', 'ARMK', 'ARNC', 'AROC', 'ARR', 'ARW', 'ASA', 'ASB', 'ASGN', 'ASH', 
    'ASIX', 'ASM', 'ASPN', 'ASR', 'ASX', 'AT', 'ATC', 'ATCO', 'ATEN', 'ATGE', 'ATH', 'ATHM', 'ATI', 'ATKR', 'ATO', 
    'ATR', 'ATTO', 'ATUS', 'AU', 'AUY', 'AVA', 'AVAL', 'AVB', 'AVD', 'AVK', 'AVLR', 'AVNS', 'AVNT', 'AVTR', 'AVY', 
    'AWI', 'AWK', 'AWR', 'AX', 'AXL', 'AXP', 'AXR', 'AXS', 'AXTA', 'AYI', 'AYX', 'AZO', 'AZRE', 'AZUL', 'AZZ', 'B', 
    'BA', 'BABA', 'BAC', 'BAH', 'BALY', 'BAM', 'BANC', 'BAP', 'BAX', 'BB', 'BBAR', 'BBD', 'BBDC', 'BBDO', 'BBL', 
    'BBU', 'BBVA', 'BBW', 'BBWI', 'BBY', 'BC', 'BCO', 'BCS', 'BCSF', 'BDC', 'BDJ', 'BDN', 'BDX', 'BE', 'BEAM', 'BEP', 
    'BERY', 'BEST', 'BF', 'BFB', 'BFK', 'BFS', 'BFZ', 'BG', 'BGB', 'BGG', 'BGH', 'BGR', 'BGS', 'BGSF', 'BGT', 'BGY', 
    'BH', 'BHC', 'BHE', 'BHK', 'BHLB', 'BHP', 'BHR', 'BHVN', 'BHVN', 'BIDU', 'BIG', 'BILL', 'BIO', 'BIOB', 'BIP', 
    'BIT', 'BITA', 'BJ', 'BKH', 'BKI', 'BKNG', 'BKR', 'BKT', 'BKU', 'BLD', 'BLCM', 'BLCN', 'BLD', 'BLE', 'BLK', 
    'BLW', 'BLX', 'BMA', 'BME', 'BMI', 'BMLP', 'BMO', 'BMRN', 'BMS', 'BMY', 'BNED', 'BNL', 'BNS', 'BNY', 'BOE', 
    'BOH', 'BOOT', 'BOX', 'BP', 'BPMP', 'BPT', 'BQ', 'BR', 'BRBR', 'BRC', 'BRFS', 'BRMK', 'BRO', 'BRP', 'BRT', 
    'BRX', 'BSAC', 'BSBR', 'BSD', 'BSE', 'BSIG', 'BSM', 'BSMX', 'BST', 'BSTZ', 'BSX', 'BTC', 'BTI', 'BTO', 'BTT', 
    'BTU', 'BTZ', 'BUD', 'BUI', 'BURL', 'BV', 'BWA', 'BWG', 'BWL', 'BXP', 'C', 'CABO', 'CACI', 'CADE', 'CAE', 'CAG', 
    'CAH', 'CAI', 'CAL', 'CALA', 'CALM', 'CALX', 'CAMP', 'CANE', 'CAPL', 'CAPR', 'CAR', 'CARS', 'CATO', 'CATY', 
    'CB', 'CBB', 'CBD', 'CBH', 'CBL', 'CBOE', 'CBRE', 'CBRL', 'CBSH', 'CBT', 'CC', 'CCJ', 'CCK', 'CCL', 'CCM', 
    'CCO', 'CCOI', 'CCS', 'CCU', 'CCX', 'CCZ', 'CDAY', 'CDR', 'CE', 'CEA', 'CECE', 'CEIX', 'CEL', 'CELG', 'CEM', 
    'CEN', 'CEO', 'CEPU', 'CEQP', 'CET', 'CETV', 'CETX', 'CFA', 'CFB', 'CFG', 'CFLT', 'CFX', 'CGA', 'CGBD', 'CGC', 
    'CGEN', 'CGIX', 'CGNX', 'CGO', 'CHA', 'CHAP', 'CHD', 'CHE', 'CHGG', 'CHH', 'CHK', 'CHKR', 'CHL', 'CHMI', 'CHN', 
    'CHRS', 'CHT', 'CHTR', 'CHU', 'CI', 'CIA', 'CIB', 'CIEN', 'CIF', 'CIG', 'CIM', 'CINF', 'CIO', 'CIR', 'CIT', 
    'CIX', 'CJ', 'CJD', 'CJJD', 'CKH', 'CL', 'CLAR', 'CLB', 'CLDR', 'CLDT', 'CLF', 'CLGX', 'CLH', 'CLI', 'CLNC', 
    'CLR', 'CLS', 'CLW', 'CLX', 'CM', 'CMA', 'CMC', 'CMCM', 'CMI', 'CMO', 'CMP', 'CMPR', 'CMS', 'CMT', 'CNA', 'CNC', 
    'CNDT', 'CNF', 'CNHI', 'CNI', 'CNK', 'CNMD', 'CNNE', 'CNO', 'CNP', 'CNR', 'CNS', 'CNX', 'CO', 'CODI', 'COE', 
    'COF', 'COG', 'COH', 'COLD', 'COO', 'COP', 'COR', 'CORT', 'COST', 'COTY', 'CP', 'CPA', 'CPAC', 'CPB', 'CPE', 
    'CPG', 'CPK', 'CPLG', 'CPLP', 'CPRI', 'CPRT', 'CPT', 'CR', 'CRAI', 'CRCM', 'CRD', 'CRH', 'CRHM', 'CRI', 'CRK', 
    'CRL', 'CRM', 'CRMD', 'CROX', 'CRS', 'CRT', 'CRTO', 'CRUS', 'CRVL', 'CRY', 'CS', 'CSAN', 'CSCO', 'CSGP', 'CSGS', 
    'CSL', 'CSM', 'CSOD', 'CSR', 'CST', 'CSTM', 'CSU', 'CSX', 'CTAA', 'CTAC', 'CTAS', 'CTB', 'CTBB', 'CTDD', 'CTEK', 
    'CTG', 'CTHR', 'CTK', 'CTL', 'CTLT', 'CTMX', 'CTS', 'CTSH', 'CTSO', 'CTT', 'CTV', 'CTVA', 'CUBI', 'CUK', 'CULL', 
    'CULP', 'CURO', 'CUTR', 'CUZ', 'CVA', 'CVE', 'CVEO', 'CVET', 'CVGI', 'CVGW', 'CVI', 'CVNA', 'CVS', 'CVX', 'CW', 
    'CWEN', 'CWH', 'CWK', 'CWT', 'CX', 'CXDC', 'CXE', 'CXH', 'CXO', 'CXP', 'CXW', 'CYD', 'CYH', 'CZR', 'D', 'DAC', 
    'DAL', 'DAN', 'DAR', 'DASH', 'DATA', 'DB', 'DBD', 'DBI', 'DBL', 'DCI', 'DCO', 'DCP', 'DD', 'DDD', 'DDF', 'DDS', 
    'DDT', 'DE', 'DEA', 'DECK', 'DEI', 'DEO', 'DESP', 'DF', 'DFIN', 'DFNS', 'DFS', 'DFT', 'DG', 'DGX', 'DHI', 'DHR', 
    'DHT', 'DHX', 'DIDI', 'DIN', 'DIS', 'DISA', 'DISCA', 'DISCB', 'DISCK', 'DISH', 'DK', 'DKL', 'DKNG', 'DKS', 
    'DLB', 'DLNG', 'DLPH', 'DLR', 'DLTH', 'DLX', 'DM', 'DMLP', 'DMO', 'DNB', 'DNK', 'DNOW', 'DNP', 'DOC', 'DOCU', 
    'DOLE', 'DOMO', 'DOOR', 'DOV', 'DPG', 'DPLO', 'DPS', 'DPW', 'DPZ', 'DQ', 'DRD', 'DRE', 'DRH', 'DRI', 'DRNA', 
    'DRQ', 'DRRX', 'DRTT', 'DS', 'DSSI', 'DSU', 'DSX', 'DT', 'DTE', 'DTF', 'DTIL', 'DTM', 'DTP', 'DTS', 'DTT', 'DUC', 
    'DUK', 'DUKH', 'DV', 'DVA', 'DVAX', 'DVD', 'DVN', 'DWIN', 'DX', 'DXB', 'DXC', 'DXF', 'DY', 'DYN', 'DYNC', 'DZSI', 
    'E', 'EA', 'EAF', 'EARN', 'EAT', 'EB', 'EBF', 'EBIX', 'EBS', 'EC', 'ECC', 'ECL', 'ECOL', 'ECPG', 'ED', 'EDD', 
    'EDF', 'EDI', 'EDIT', 'EDN', 'EDR', 'EDU', 'EE', 'EEFT', 'EEIQ', 'EEX', 'EFC', 'EFF', 'EFL', 'EFSC', 'EGBN', 
    'EGF', 'EGHT', 'EGP', 'EGY', 'EH', 'EHC', 'EHI', 'EHIC', 'EHT', 'EHTH', 'EI', 'EIC', 'EIG', 'EIX', 'EKSO', 
    'EL', 'ELA', 'ELAN', 'ELAT', 'ELF', 'ELLO', 'ELMD', 'ELP', 'ELS', 'ELTK', 'ELV', 'EMD', 'EME', 'EMF', 'EMIT', 
    'EMMS', 'EMN', 'EMO', 'EMP', 'EMR', 'ENBL', 'ENB', 'ENDP', 'ENIA', 'ENIC', 'ENJ', 'ENLC', 'ENR', 'ENS', 'ENV', 
    'ENVA', 'ENZ', 'EOG', 'EOI', 'EOS', 'EP', 'EPAC', 'EPAM', 'EPD', 'EPR', 'EPRT', 'EPS', 'EPU', 'EQ', 'EQC', 
    'EQH', 'EQIX', 'EQNR', 'EQR', 'EQS', 'EQT', 'EQX', 'ERF', 'ERH', 'ERII', 'ES', 'ESBA', 'ESCA', 'ESE', 'ESGC', 
    'ESI', 'ESL', 'ESLT', 'ESNT', 'ESPP', 'ESS', 'ET', 'ETB', 'ETD', 'ETE', 'ETG', 'ETH', 'ETJ', 'ETN', 'ETO', 
    'ETP', 'ETR', 'ETRN', 'ETS', 'ETV', 'ETW', 'ETY', 'EUCR', 'EURN', 'EVA', 'EVC', 'EVE', 'EVF', 'EVG', 'EVH', 
    'EVK', 'EVLO', 'EVN', 'EVO', 'EVR', 'EVRG', 'EVRI', 'EVT', 'EVTC', 'EW', 'EXAS', 'EXC', 'EXD', 'EXG', 'EXK', 
    'EXLS', 'EXP', 'EXPE', 'EXPI', 'EXR', 'EXTN', 'EXTR', 'EYE', 'EYES', 'EYH', 'EYPT', 'EZJ', 'EZPW', 'F', 'FAF', 
    'FAM', 'FANH', 'FBC', 'FBHS', 'FBK', 'FBP', 'FBZ', 'FC', 'FCAP', 'FCF', 'FCFS', 'FCN', 'FCPT', 'FCRD', 'FCSC', 
    'FCT', 'FCX', 'FDC', 'FDEU', 'FDP', 'FDS', 'FDX', 'FE', 'FEAC', 'FED', 'FENG', 'FET', 'FF', 'FFA', 'FFC', 'FFG', 
    'FFHL', 'FFIN', 'FFIV', 'FFNW', 'FFWM', 'FG', 'FGB', 'FHB', 'FHI', 'FHN', 'FI', 'FICO', 'FIF', 'FIGS', 'FINV', 
    'FINX', 'FIS', 'FISI', 'FISV', 'FITB', 'FITBO', 'FITBP', 'FIV', 'FIX', 'FIZZ', 'FL', 'FLGT', 'FLL', 'FLMN', 
    'FLNG', 'FLR', 'FLS', 'FLT', 'FLWS', 'FLXN', 'FLXS', 'FLY', 'FMC', 'FMN', 'FMX', 'FMY', 'FN', 'FNB', 'FNCB', 
    'FNF', 'FNHC', 'FNGU', 'FNF', 'FNLC', 'FNX', 'FOCS', 'FOE', 'FOF', 'FOR', 'FORA', 'FORD', 'FORR', 'FOSL', 
    'FOX', 'FOXA', 'FOXF', 'FPI', 'FPL', 'FR', 'FRA', 'FRC', 'FRED', 'FRF', 'FRG', 'FRHC', 'FRI', 'FRLG', 'FRME', 
    'FRO', 'FRT', 'FRTA', 'FRW', 'FSB', 'FSBC', 'FSBW', 'FSD', 'FSEA', 'FSEP', 'FSFG', 'FSI', 'FSK', 'FSLR', 
    'FSM', 'FSV', 'FTAI', 'FTCH', 'FTD', 'FTEK', 'FTHY', 'FTI', 'FTK', 'FTNT', 'FTOC', 'FTSI', 'FTV', 'FUBO', 'FUL', 
    'FULT', 'FUN', 'FUSB', 'FUTU', 'FV', 'FVE', 'FVIV', 'FVRR', 'FWAA', 'FWAC', 'FWONA', 'FXL', 'FXNC', 'G', 'GAB', 
    'GABC', 'GAIA', 'GAIN', 'GAU', 'GCP', 'GD', 'GDDY', 'GDEN', 'GDI', 'GE', 'GEF', 'GEG', 'GEN', 'GEO', 'GEP', 
    'GER', 'GES', 'GEVO', 'GF', 'GFF', 'GFL', 'GGB', 'GGG', 'GGV', 'GHL', 'GHM', 'GHSI', 'GHY', 'GIC', 'GIL', 
    'GIM', 'GIS', 'GJH', 'GJO', 'GJP', 'GJS', 'GJT', 'GJV', 'GL', 'GLA', 'GLAD', 'GLBS', 'GLDD', 'GLG', 'GLO', 
    'GLP', 'GLPI', 'GLRE', 'GLT', 'GLUU', 'GLW', 'GM', 'GMED', 'GMRE', 'GMS', 'GNE', 'GNK', 'GNL', 'GNRC', 'GNT', 
    'GNW', 'GO', 'GOGO', 'GOLD', 'GOLF', 'GOOD', 'GOOG', 'GOOGL', 'GORO', 'GOTU', 'GOV', 'GPC', 'GPI', 'GPK', 
    'GPN', 'GPRK', 'GPS', 'GRBK', 'GRFS', 'GRIL', 'GRMN', 'GROW', 'GRP', 'GRUB', 'GRX', 'GS', 'GSH', 'GSK', 'GSL', 
    'GSVC', 'GT', 'GTE', 'GTES', 'GTLS', 'GTN', 'GTS', 'GTT', 'GTY', 'GUT', 'GVA', 'GWB', 'GWRE', 'GWW', 'GXC', 
    'GXO', 'GYB', 'GYC', 'H', 'HA', 'HAE', 'HAFC', 'HAIN', 'HAL', 'HALO', 'HASI', 'HAYN', 'HBB', 'HBI', 'HBM', 
    'HCA', 'HCC', 'HCI', 'HCKT', 'HCSG', 'HD', 'HDB', 'HE', 'HEI', 'HELE', 'HEP', 'HEQ', 'HES', 'HF', 'HFC', 'HFRO', 
    'HGH', 'HGV', 'HHC', 'HHS', 'HI', 'HIBB', 'HIE', 'HIFS', 'HIG', 'HII', 'HIL', 'HIMX', 'HIO', 'HITI', 'HIVE', 
    'HIW', 'HIX', 'HLI', 'HLIO', 'HLIT', 'HLS', 'HLT', 'HLX', 'HMC', 'HMLP', 'HMN', 'HMY', 'HNI', 'HNRG', 'HNW', 
    'HOFT', 'HOG', 'HOLI', 'HOLX', 'HOMB', 'HON', 'HOPE', 'HOS', 'HOTL', 'HOV', 'HP', 'HPE', 'HPF', 'HPI', 'HPP', 
    'HPQ', 'HPS', 'HPX', 'HQH', 'HQL', 'HR', 'HRB', 'HRC', 'HRL', 'HRT', 'HRTX', 'HRZN', 'HSBC', 'HSC', 'HST', 
    'HSY', 'HT', 'HTA', 'HTBK', 'HTD', 'HTGC', 'HTH', 'HTY', 'HUBB', 'HUBG', 'HUBS', 'HUD', 'HUM', 'HUN', 'HURC', 
    'HURN', 'HUSA', 'HVT', 'HW', 'HWM', 'HXL', 'HY', 'HYB', 'HYD', 'HYI', 'HYMC', 'HYT', 'HYXU', 'HZO', 'IAC', 'IAE', 
    'IAF', 'IAG', 'IBA', 'IBM', 'IBN', 'IBOC', 'IBP', 'ICD', 'ICE', 'ICHR', 'ICL', 'ICLN', 'ICLR', 'ICON', 'ICR', 
    'ICU', 'IDA', 'IDE', 'IDN', 'IDT', 'IDXX', 'IE', 'IEA', 'IEC', 'IEF', 'IEI', 'IEX', 'IFF', 'IFGL', 'IFN', 'IFR', 
    'IFS', 'IGA', 'IGD', 'IGE', 'IGI', 'IGM', 'IGN', 'IGR', 'IGT', 'IH', 'IHC', 'IHG', 'IHT', 'IID', 'IIF', 'IIM', 
    'IIN', 'IIPR', 'IMAX', 'IMH', 'IMMR', 'IMMU', 'IMPV', 'IMRN', 'IMUX', 'IMXI', 'IN', 'INA', 'INCY', 'INDB', 
    'INDO', 'INFI', 'INFN', 'INFO', 'INFY', 'ING', 'INGN', 'INN', 'INNV', 'INO', 'INPX', 'INS', 'INSE', 'INSI', 
    'INSM', 'INST', 'INSW', 'INSY', 'INT', 'INTEQ', 'INTL', 'INTT', 'INTU', 'INUV', 'INVA', 'INVH', 'INXN', 'IO', 
    'IOI', 'IOR', 'IOSP', 'IP', 'IPAR', 'IPD', 'IPG', 'IPGP', 'IPHI', 'IPIC', 'IPOF', 'IPV', 'IQ', 'IQI', 'IQV', 
    'IR', 'IRBT', 'IRM', 'IRR', 'IRS', 'IRT', 'IRWD', 'ISD', 'ISDR', 'ISG', 'ISHG', 'ISIG', 'ISNPY', 'ISR', 'ISRG', 
    'IT', 'ITA', 'ITB', 'ITCB', 'ITGR', 'ITI', 'ITM', 'ITP', 'ITR', 'ITRI', 'ITT', 'ITUB', 'ITW', 'IVAC', 'IVC', 
    'IVH', 'IVR', 'IVZ', 'IX', 'JACK', 'JAGX', 'JAKK', 'JASN', 'JAX', 'JAZZ', 'JBGS', 'JBHT', 'JBL', 'JBLU', 'JBN', 
    'JBR', 'JBT', 'JCAP', 'JCE', 'JCI', 'JCOM', 'JCPNQ', 'JCS', 'JCTCF', 'JD', 'JDD', 'JEF', 'JELD', 'JEMD', 'JFR', 
    'JGH', 'JGV', 'JHB', 'JHG', 'JHI', 'JHS', 'JHX', 'JILL', 'JJSF', 'JKHY', 'JKI', 'JKS', 'JLL', 'JLS', 'JMEI', 
    'JMF', 'JMLP', 'JMM', 'JMP', 'JNJ', 'JNPR', 'JOAN', 'JOB', 'JOBS', 'JOF', 'JOUT', 'JP', 'JPC', 'JPIC', 'JPM', 
    'JPS', 'JPT', 'JQC', 'JRI', 'JRJC', 'JRO', 'JRS', 'JSD', 'JSG', 'JSH', 'JSM', 'JSMD', 'JSYN', 'JT', 'JTA', 'JTD', 
    'JVA', 'JVAL', 'JW', 'JW.A', 'JW.B', 'JWN', 'JXSB', 'K', 'KAI', 'KALV', 'KAMN', 'KAR', 'KB', 'KBH', 'KBR', 
    'KDMN', 'KDUS', 'KEM', 'KEN', 'KEP', 'KEQU', 'KERX', 'KEX', 'KEY', 'KEYS', 'KF', 'KFFB', 'KFRC', 'KFY', 'KGC', 
    'KHC', 'KIM', 'KIM-A', 'KIML', 'KIMN', 'KINS', 'KIO', 'KIRK', 'KJUN', 'KKR', 'KL', 'KMB', 'KMF', 'KMI', 'KMM', 
    'KMPH', 'KMT', 'KMX', 'KN', 'KNL', 'KNOP', 'KNSL', 'KNX', 'KO', 'KODK', 'KOF', 'KOP', 'KOPN', 'KOS', 'KRA', 
    'KRC', 'KRG', 'KRO', 'KRP', 'KSM', 'KSS', 'KSU', 'KTB', 'KTOS', 'KTOV', 'KTP', 'KURA', 'KVHI', 'KW', 'KWR', 
    'KYN', 'KZR', 'L', 'LABL', 'LAC', 'LADR', 'LADU', 'LADR', 'LAIX', 'LAMR', 'LANC', 'LAND', 'LARK', 'LAUR', 'LAWS', 
    'LBAI', 'LB', 'LBC', 'LBRDA', 'LBRDB', 'LBRDK', 'LBTYA', 'LBTYB', 'LBTYK', 'LC', 'LCI', 'LCII', 'LCM', 'LCTX', 
    'LCUT', 'LDL', 'LDOS', 'LDP', 'LDSF', 'LEA', 'LEAF', 'LEAF', 'LECO', 'LEDS', 'LEE', 'LEG', 'LEJU', 'LEN', 'LEVI', 
    'LEXX', 'LFAC', 'LFAC', 'LFAC', 'LFC', 'LFL', 'LFST', 'LGF', 'LGF.A', 'LGF.B', 'LGND', 'LH', 'LHCG', 'LHC', 
    'LHX', 'LII', 'LILA', 'LILAK', 'LIN', 'LIND', 'LINX', 'LITB', 'LIVE', 'LIVN', 'LIVX', 'LK', 'LKCO', 'LKFN', 'LKQ', 
    'LL', 'LLY', 'LM', 'LMAT', 'LMB', 'LMFA', 'LMNR', 'LMNX', 'LMT', 'LNC', 'LNG', 'LNN', 'LNT', 'LNW', 'LOAC', 
    'LOAN', 'LOB', 'LODE', 'LOGI', 'LOOP', 'LOPE', 'LORL', 'LOVE', 'LOW', 'LPCN', 'LPG', 'LPI', 'LPL', 'LPLA', 'LPX', 
    'LQD', 'LQDA', 'LQDT', 'LRAD', 'LRFC', 'LRN', 'LSBK', 'LSI', 'LSXMA', 'LSXMB', 'LSXMK', 'LTC', 'LTHM', 'LTRPA', 
    'LTRPB', 'LUB', 'LUMN', 'LUNA', 'LUV', 'LVS', 'LW', 'LX', 'LXFR', 'LXP', 'LXP-C', 'LXRX', 'LYB', 'LYG', 'LYTS', 
    'LYV', 'LZB', 'M', 'MA', 'MAA', 'MAC', 'MAG', 'MAIN', 'MAN', 'MANU', 'MAS', 'MAT', 'MATX', 'MAXR', 'MBB', 
    'MBCN', 'MBI', 'MBII', 'MBIN', 'MBOT', 'MBRX', 'MBT', 'MBWM', 'MC', 'MCA', 'MCAC', 'MCBC', 'MCB', 'MCC', 'MCD', 
    'MCEP', 'MCF', 'MCFT', 'MCHP', 'MCHX', 'MCI', 'MCK', 'MCO', 'MCR', 'MCRB', 'MCRI', 'MCS', 'MCV', 'MCX', 'MD', 
    'MDC', 'MDGL', 'MDGS', 'MDLZ', 'MDP', 'MDR', 'MDRR', 'MDRX', 'MDSO', 'MDT', 'MDU', 'MDWD', 'MDXG', 'MED', 'MEET', 
    'MEG', 'MEI', 'MEIP', 'MELI', 'MELT', 'MEN', 'MEOH', 'MER', 'MET', 'MFA', 'MFA-B', 'MFA-C', 'MFAC', 'MFC', 'MFD', 
    'MFG', 'MFGP', 'MFIN', 'MFNC', 'MFO', 'MFT', 'MFV', 'MG', 'MGA', 'MGEE', 'MGF', 'MGI', 'MGIC', 'MGM', 'MGN', 
    'MGP', 'MGRC', 'MGTA', 'MGTX', 'MGY', 'MHD', 'MHF', 'MHI', 'MHK', 'MHLD', 'MHN', 'MHO', 'MIC', 'MICR', 'MICT', 
    'MIDD', 'MIE', 'MII', 'MIII', 'MIK', 'MILN', 'MIME', 'MIN', 'MINC', 'MIND', 'MINDP', 'MINI', 'MIO', 'MIR', 'MITK', 
    'MITT', 'MITT-A', 'MITT-B', 'MITT-C', 'MIXT', 'MIY', 'MJ', 'MJL', 'MJNE', 'MJN', 'MKC', 'MKC.V', 'MKL', 'MKSI', 
    'MKT', 'ML', 'MLAB', 'MLAC', 'MLACU', 'MLACW', 'MLHR', 'MLI', 'MLKN', 'MLM', 'MLNK', 'MLNX', 'MLP', 'MLR', 'MLVF', 
    'MM', 'MMAC', 'MMC', 'MMI', 'MMLP', 'MMM', 'MMP', 'MMT', 'MMU', 'MMX', 'MMYT', 'MN', 'MNA', 'MNDO', 'MNGA', 'MNK', 
    'MNKD', 'MNLO', 'MNP', 'MNR', 'MNR-C', 'MNRO', 'MNST', 'MNTA', 'MNTX', 'MO', 'MOD', 'MODN', 'MOFG', 'MOG.A', 
    'MOG.B', 'MOGO', 'MOH', 'MOMO', 'MON', 'MONC', 'MOO', 'MOR', 'MOS', 'MOV', 'MOXC', 'MP', 'MPAC', 'MPA', 'MPAA', 
    'MPB', 'MPC', 'MPLX', 'MPO', 'MPR', 'MPT', 'MPV', 'MPW', 'MPWR', 'MPX', 'MQU', 'MQY', 'MR', 'MRA', 'MRAM', 'MRBK', 
    'MRC', 'MRCC', 'MRCY', 'MREO', 'MRK', 'MRLN', 'MRM', 'MRNA', 'MRNS', 'MRO', 'MRSN', 'MRT', 'MRTN', 'MRTX', 
    'MRUS', 'MRVI', 'MRVL', 'MS', 'MSA', 'MSB', 'MSBI', 'MSC', 'MSCC', 'MSCI', 'MSD', 'MSEX', 'MSFG', 'MSFT', 'MSGE', 
    'MSGS', 'MSI', 'MSM', 'MSN', 'MSP', 'MSVB', 'MT', 'MTB', 'MTBC', 'MTBCP', 'MTCH', 'MTD', 'MTDR', 'MTEM', 'MTG', 
    'MTH', 'MTN', 'MTOR', 'MTP', 'MTR', 'MTRN', 'MTRX', 'MTS', 'MTSC', 'MTSI', 'MTW', 'MTX', 'MTZ', 'MU', 'MUA', 
    'MUC', 'MUE', 'MUFG', 'MUH', 'MUI', 'MUJ', 'MUR', 'MUS', 'MUX', 'MVBF', 'MVC', 'MVF', 'MVO', 'MVT', 'MWA', 
    'MWC', 'MX', 'MXC', 'MXE', 'MXF', 'MXIM', 'MXL', 'MYC', 'MYD', 'MYE', 'MYF', 'MYI', 'MYJ', 'MYN', 'MYO', 'MYOV', 
    'MYRG', 'MYSZ', 'MYT', 'MZA', 'NAC', 'NAD', 'NAII', 'NAIL', 'NAK', 'NAN', 'NAO', 'NAPA', 'NARI', 'NAT', 'NAV', 
    'NAVI', 'NAZ', 'NBB', 'NBHC', 'NBIX', 'NBN', 'NBO', 'NBR', 'NBR-A', 'NBRV', 'NBTB', 'NBW', 'NBY', 'NC', 'NCA', 
    'NCB', 'NCBS', 'NCI', 'NCLH', 'NCMI', 'NCNA', 'NCV', 'NCZ', 'ND', 'NDP', 'NDRA', 'NDRAW', 'NDSN', 'NE', 'NEA', 
    'NEE', 'NEE-I', 'NEE-J', 'NEE-K', 'NEE-Q', 'NEE-R', 'NEE-S', 'NEE-T', 'NEM', 'NEO', 'NEON', 'NEOS', 'NEP', 'NEPT', 
    'NERV', 'NES', 'NESR', 'NET', 'NETE', 'NEU', 'NEV', 'NEW', 'NEWA', 'NEWM', 'NEWR', 'NEX', 'NEXA', 'NEXT', 'NFBK', 
    'NFC', 'NFJ', 'NFLT', 'NFLX', 'NFZ', 'NGG', 'NGL', 'NGM', 'NGS', 'NGVC', 'NGVT', 'NHA', 'NHF', 'NHHS', 'NHI', 
    'NHS', 'NHTC', 'NI', 'NID', 'NIM', 'NINE', 'NIO', 'NIQ', 'NJR', 'NKE', 'NKG', 'NKSH', 'NKTR', 'NKX', 'NL', 
    'NLOK', 'NLS', 'NLSN', 'NLY', 'NLY-D', 'NLY-F', 'NLY-G', 'NLY-I', 'NM', 'NMFC', 'NMI', 'NMM', 'NMR', 'NMS', 
    'NMT', 'NMY', 'NMZ', 'NNA', 'NNBR', 'NNC', 'NNI', 'NNN', 'NNVC', 'NOA', 'NOAH', 'NOC', 'NODK', 'NOG', 'NOK', 
    'NOM', 'NOMD', 'NOR', 'NOV', 'NOVA', 'NOW', 'NP', 'NPK', 'NPN', 'NPO', 'NPTN', 'NPV', 'NQP', 'NR', 'NRC', 
    'NREF', 'NRG', 'NRGX', 'NRIM', 'NRK', 'NRO', 'NRP', 'NRT', 'NRUC', 'NRZ', 'NRZ-A', 'NRZ-B', 'NRZ-C', 'NS', 'NSA', 
    'NSC', 'NSEC', 'NSIT', 'NSL', 'NSP', 'NSPR', 'NSR', 'NSS', 'NTB', 'NTC', 'NTCO', 'NTG', 'NTIP', 'NTLA', 'NTNX', 
    'NTP', 'NTR', 'NTRA', 'NTRS', 'NTST', 'NTZ', 'NUE', 'NUM', 'NUO', 'NURO', 'NUS', 'NUTX', 'NUV', 'NUW', 'NVG', 
    'NVGS', 'NVI', 'NVMI', 'NVO', 'NVR', 'NVRO', 'NVS', 'NVST', 'NVT', 'NVTA', 'NWE', 'NWG', 'NWHM', 'NWN', 'NWPX', 
    'NWS', 'NWSA', 'NX', 'NXC', 'NXN', 'NXP', 'NXQ', 'NXR', 'NXRT', 'NYC', 'NYCB', 'NYT', 'NYV', 'NZF', 'O', 'OA', 
    'OAC', 'OAK', 'OAK-A', 'OAK-B', 'OAS', 'OASM', 'OBAS', 'OBCI', 'OBE', 'OBLG', 'OC', 'OCFT', 'OCN', 'ODC', 
    'ODFL', 'ODP', 'ODT', 'OEC', 'OEF', 'OFC', 'OFED', 'OFG', 'OFS', 'OGE', 'OGEN', 'OGI', 'OGS', 'OHI', 'OI', 'OIA', 
    'OIBR', 'OIH', 'OII', 'OIS', 'OKE', 'OKTA', 'OLB', 'OLED', 'OLK', 'OLN', 'OLP', 'OMC', 'OMF', 'OMI', 'OMP', 'ON', 
    'ONB', 'ONCR', 'ONDK', 'ONE', 'ONTO', 'ONTX', 'ONVO', 'OOMA', 'OP', 'OPA', 'OPBK', 'OPCH', 'OPEN', 'OPGN', 'OPI', 
    'OPK', 'OPNT', 'OPOF', 'OPP', 'OPRA', 'OPRX', 'OPT', 'OPTN', 'OPY', 'OR', 'ORA', 'ORAN', 'ORC', 'ORCC', 'ORCL', 
    'ORI', 'ORLA', 'ORN', 'OSB', 'OSG', 'OSIS', 'OSK', 'OSMT', 'OSPN', 'OSS', 'OSTK', 'OSUR', 'OTEL', 'OTEX', 'OTIS', 
    'OTLK', 'OTR', 'OTRK', 'OUT', 'OVBC', 'OVID', 'OVLY', 'OXBR', 'OXFD', 'OXLC', 'OXLCM', 'OXLCN', 'OXLCO', 'OXY', 
    'OZK', 'P', 'PAC', 'PACB', 'PACD', 'PACE', 'PACK', 'PACQ', 'PAG', 'PAGS', 'PAH', 'PAI', 'PAM', 'PANL', 'PAPR', 
    'PAR', 'PARR', 'PATI', 'PATK', 'PAVM', 'PAY', 'PAYC', 'PAYS', 'PB', 'PBA', 'PBB', 'PBC', 'PBCT', 'PBF', 'PBFX', 
    'PBH', 'PBI', 'PBR', 'PBT', 'PBYI', 'PCAR', 'PCB', 'PCCC', 'PCF', 'PCG', 'PCH', 'PCI', 'PCK', 'PCM', 'PCN', 
    'PCOM', 'PCOR', 'PCQ', 'PCRX', 'PCSB', 'PCTI', 'PCTY', 'PCYG', 'PCYO', 'PD', 'PDCE', 'PDCO', 'PDI', 'PDLI', 
    'PDM', 'PDS', 'PDX', 'PE', 'PEAK', 'PEB', 'PEBO', 'PEG', 'PEI', 'PEN', 'PEO', 'PEP', 'PER', 'PES', 'PETQ', 'PETS', 
    'PFBC', 'PFD', 'PFE', 'PFG', 'PFGC', 'PFH', 'PFIE', 'PFIN', 'PFIS', 'PFL', 'PFLT', 'PFN', 'PFPT', 'PFS', 'PFSI', 
    'PFSW', 'PFXF', 'PG', 'PGC', 'PGEN', 'PGNY', 'PGP', 'PGR', 'PGRE', 'PGTI', 'PGZ', 'PH', 'PHD', 'PHG', 'PHI', 
    'PHK', 'PHM', 'PHT', 'PHX', 'PI', 'PIAI', 'PICO', 'PID', 'PIH', 'PII', 'PIKE', 'PIM', 'PINC', 'PINE', 'PING', 
    'PINS', 'PIO', 'PIPR', 'PIR', 'PIRS', 'PIY', 'PJC', 'PJT', 'PK', 'PKE', 'PKG', 'PKI', 'PKO', 'PKOH', 'PKX', 
    'PLAN', 'PLBC', 'PLD', 'PLG', 'PLIN', 'PLL', 'PLM', 'PLMR', 'PLNT', 'PLOW', 'PLPC', 'PLRX', 'PLSE', 'PLT', 'PLUG', 
    'PLUS', 'PLX', 'PLXP', 'PM', 'PMBC', 'PMD', 'PME', 'PMF', 'PMGM', 'PMH', 'PML', 'PMM', 'PMO', 'PMT', 'PMX', 
    'PNBK', 'PNC', 'PNF', 'PNFP', 'PNI', 'PNM', 'PNNT', 'PNR', 'PNRG', 'PNW', 'POAI', 'PODD', 'POL', 'POLA', 'POOL', 
    'POR', 'POST', 'POWI', 'POWL', 'PPBI', 'PPG', 'PPL', 'PPR', 'PPSI', 'PPT', 'PPX', 'PQG', 'PRA', 'PRAA', 'PRAH', 
    'PRCP', 'PRDO', 'PRFT', 'PRFZ', 'PRGO', 'PRGX', 'PRH', 'PRI', 'PRIM', 'PRK', 'PRLB', 'PRMW', 'PRO', 'PROC', 'PROF', 
    'PROV', 'PRPB', 'PRPH', 'PRPL', 'PRPO', 'PRQR', 'PRS', 'PRTA', 'PRTH', 'PRTK', 'PRTS', 'PRTY', 'PRU', 'PRVL', 
    'PRY', 'PRY-A', 'PS', 'PSA', 'PSA-A', 'PSA-B', 'PSA-C', 'PSA-D', 'PSA-E', 'PSA-F', 'PSA-G', 'PSA-H', 'PSA-I', 
    'PSA-J', 'PSA-K', 'PSA-L', 'PSA-M', 'PSA-N', 'PSA-O', 'PSA-P', 'PSA-Q', 'PSA-R', 'PSA-S', 'PSA-T', 'PSA-U', 
    'PSA-V', 'PSA-W', 'PSA-X', 'PSA-Y', 'PSA-Z', 'PSB', 'PSB-W', 'PSB-X', 'PSB-Y', 'PSB-Z', 'PSF', 'PSFE', 'PSHZF', 
    'PSMT', 'PSN', 'PSO', 'PSTG', 'PSTL', 'PSX', 'PSXP', 'PTA', 'PTAC', 'PTC', 'PTCT', 'PTE', 'PTEN', 'PTH', 'PTK', 
    'PTLA', 'PTMN', 'PTN', 'PTNR', 'PTON', 'PTR', 'PTRY', 'PTSI', 'PTVCA', 'PTVCB', 'PTY', 'PUK', 'PUK-A', 'PUK-B', 
    'PULM', 'PUMP', 'PUT', 'PVAC', 'PVAL', 'PVBC', 'PVG', 'PVH', 'PVI', 'PVL', 'PVLT', 'PW', 'PW-A', 'PWOD', 'PWR', 
    'PWV', 'PWZ', 'PXD', 'PXF', 'PXLW', 'PXQ', 'PXS', 'PY', 'PYN', 'PYPD', 'PYPL', 'PYS', 'PYT', 'PYX', 'PZC', 'PZN', 
    'PZT', 'QADA', 'QADB', 'QAF', 'QAN', 'QAT', 'QCLN', 'QCRH', 'QD', 'QDEL', 'QEP', 'QGEN', 'QH', 'QHC', 'QID', 
    'QIWI', 'QLGN', 'QLYS', 'QNST', 'QRHC', 'QRTEA', 'QRTEB', 'QRVO', 'QSR', 'QSY', 'QTS', 'QTS-A', 'QTS-B', 'QTWO', 
    'QUAD', 'QUIK', 'QUMU', 'QUOT', 'QURE', 'QVCC', 'QVCM', 'QVCD', 'QYLD', 'R', 'RA', 'RAAX', 'RAIL', 'RAMP', 'RBA', 
    'RBC', 'RBCAA', 'RBLX', 'RC', 'RCA', 'RCB', 'RCI', 'RCL', 'RCP', 'RCUS', 'RDA', 'RDBX', 'RDN', 'RDNT', 'RDS', 
    'RDUS', 'RDVT', 'RDWR', 'RDY', 'RE', 'REAL', 'RECN', 'REDU', 'REE', 'REED', 'REFR', 'REG', 'REGI', 'REI', 'REIS', 
    'REKR', 'RELY', 'RELX', 'RENN', 'RENN', 'REPH', 'RES', 'RESI', 'RETA', 'REV', 'REVG', 'REX', 'REXR', 'REYN', 'RF', 
    'RF-A', 'RF-B', 'RFI', 'RFL', 'RFM', 'RFMZ', 'RFP', 'RGA', 'RGC', 'RGCO', 'RGEN', 'RGF', 'RGLB', 'RGLD', 'RGLS', 
    'RGNX', 'RGP', 'RGR', 'RGS', 'RGT', 'RH', 'RHE', 'RHI', 'RHP', 'RIBT', 'RICE', 'RICK', 'RIDE', 'RIG', 'RIGL', 
    'RILY', 'RILYG', 'RILYH', 'RILYI', 'RILYM', 'RILYN', 'RILYO', 'RILYP', 'RILYT', 'RILYZ', 'RIO', 'RIOT', 'RIV', 
    'RJF', 'RKDA', 'RL', 'RLH', 'RLJ', 'RLMD', 'RLTY', 'RLX', 'RLY', 'RM', 'RMAX', 'RMBI', 'RMBL', 'RMBS', 'RMCF', 
    'RMD', 'RMED', 'RMI', 'RMM', 'RMMZ', 'RMO', 'RMP', 'RMPL', 'RMR', 'RMT', 'RMTI', 'RNA', 'RNAZ', 'RNE', 'RNG', 
    'RNGR', 'RNLX', 'RNP', 'RNR', 'RNR-F', 'RNR-G', 'RNR-H', 'RNS', 'RNST', 'RNWK', 'ROAD', 'ROC', 'ROG', 'ROIC', 
    'ROK', 'ROKT', 'ROL', 'ROLL', 'RONI', 'ROOF', 'ROP', 'ROSE', 'ROST', 'ROVR', 'RP', 'RPAI', 'RPLA', 'RPT', 'RQI', 
    'RRC', 'RRD', 'RRGB', 'RRR', 'RS', 'RSG', 'RSI', 'RSPP', 'RSSS', 'RSVA', 'RTAI', 'RTP', 'RTPZ', 'RUBY', 'RUN', 
    'RUSHA', 'RUSHB', 'RUSL', 'RUTH', 'RVLV', 'RVMD', 'RVNC', 'RVP', 'RVSB', 'RVT', 'RWAY', 'RWLK', 'RWOD', 'RWT', 
    'RXD', 'RXI', 'RXN', 'RY', 'RY-T', 'RYAAY', 'RYAM', 'RYB', 'RYCE', 'RYF', 'RYH', 'RYI', 'RYN', 'RYT', 'RYU', 
    'RYTM', 'RZA', 'RZG', 'RZV', 'SA', 'SAB', 'SACC', 'SACH', 'SAFE', 'SAFM', 'SAFT', 'SAGE', 'SAH', 'SAIA', 'SAIC', 
    'SAIL', 'SAL', 'SALM', 'SALT', 'SAM', 'SAN', 'SANA', 'SAND', 'SASR', 'SATS', 'SAVA', 'SAVE', 'SB', 'SBAC', 'SBBA', 
    'SBBP', 'SBCF', 'SBFG', 'SBGI', 'SBI', 'SBK', 'SBND', 'SBNY', 'SBOW', 'SBR', 'SBS', 'SBSI', 'SBSW', 'SBT', 
    'SBUX', 'SC', 'SCA', 'SCC', 'SCCO', 'SCD', 'SCHL', 'SCHN', 'SCHW', 'SCI', 'SCKT', 'SCL', 'SCM', 'SCOR', 'SCS', 
    'SCTO', 'SCU', 'SCVL', 'SCWX', 'SCX', 'SCYX', 'SD', 'SDC', 'SDGR', 'SDH', 'SDPI', 'SE', 'SEAC', 'SEAH', 'SEAS', 
    'SEB', 'SECO', 'SEDG', 'SEE', 'SEEL', 'SEIC', 'SELB', 'SEM', 'SEMG', 'SENS', 'SERV', 'SESN', 'SF', 'SF-A', 'SFB', 
    'SFBC', 'SFE', 'SFIX', 'SFL', 'SFM', 'SFNC', 'SFT', 'SFUN', 'SGA', 'SGB', 'SGC', 'SGEN', 'SGG', 'SGH', 'SGL', 
    'SGMO', 'SGMS', 'SGOC', 'SGP', 'SGRY', 'SGU', 'SGZA', 'SHAK', 'SHB', 'SHBI', 'SHC', 'SHEN', 'SHG', 'SHI', 'SHIP', 
    'SHLL', 'SHLO', 'SHLX', 'SHO', 'SHOP', 'SHO-F', 'SHOO', 'SHW', 'SI', 'SIBN', 'SID', 'SIEB', 'SIEN', 'SIF', 
    'SIG', 'SIGI', 'SII', 'SILK', 'SILV', 'SIM', 'SINA', 'SINO', 'SINT', 'SIOX', 'SIRI', 'SITC', 'SITE', 'SITK', 
    'SIVB', 'SIX', 'SJ', 'SJI', 'SJM', 'SJR', 'SJT', 'SJW', 'SKE', 'SKM', 'SKT', 'SKX', 'SKY', 'SKYS', 'SKYW', 'SLAB', 
    'SLB', 'SLCA', 'SLDB', 'SLF', 'SLG', 'SLGG', 'SLGN', 'SLM', 'SLMBP', 'SLN', 'SLNG', 'SLNO', 'SLP', 'SLQT', 'SLRC', 
    'SLS', 'SLT', 'SLVO', 'SLX', 'SM', 'SMAR', 'SMBC', 'SMBK', 'SMCI', 'SMG', 'SMHI', 'SMID', 'SMIT', 'SMLP', 'SMM', 
    'SMMF', 'SMP', 'SMPL', 'SMRT', 'SMS', 'SMTA', 'SMTC', 'SMTS', 'SMTX', 'SNA', 'SNAP', 'SNBR', 'SNCR', 'SND', 
    'SNDA', 'SNDX', 'SNE', 'SNFCA', 'SNGX', 'SNLN', 'SNMP', 'SNN', 'SNP', 'SNPR', 'SNPS', 'SNSR', 'SNV', 'SNV-C', 
    'SNV-D', 'SNV-E', 'SNX', 'SNY', 'SO', 'SOGO', 'SOHU', 'SOI', 'SOJA', 'SOJB', 'SOJC', 'SOL', 'SOLN', 'SOLO', 'SON', 
    'SONM', 'SONN', 'SONO', 'SOR', 'SOS', 'SP', 'SPA', 'SPB', 'SPCE', 'SPFI', 'SPG', 'SPGI', 'SPH', 'SPHS', 'SPI', 
    'SPKE', 'SPLK', 'SPN', 'SPNS', 'SPNT', 'SPOK', 'SPOT', 'SPR', 'SPRO', 'SPSC', 'SPT', 'SPTN', 'SPWH', 'SPXC', 
    'SQ', 'SQBG', 'SQM', 'SQNS', 'SQR', 'SQQQ', 'SQZ', 'SR', 'SR-A', 'SR-B', 'SR-C', 'SR-D', 'SR-E', 'SR-F', 'SRAC', 
    'SRC', 'SRE', 'SREA', 'SREV', 'SRF', 'SRG', 'SRI', 'SRLP', 'SRNE', 'SRPT', 'SRRA', 'SRRK', 'SRT', 'SRTS', 'SRV', 
    'SSD', 'SSKN', 'SSL', 'SSNC', 'SSNT', 'SSP', 'SSRM', 'SSSS', 'SSTK', 'SSY', 'SSYS', 'ST', 'STAA', 'STAF', 'STAG', 
    'STAR', 'STAY', 'STBA', 'STC', 'STE', 'STEM', 'STEP', 'STFC', 'STG', 'STIM', 'STK', 'STKL', 'STKS', 'STL', 'STLA', 
    'STLD', 'STM', 'STMP', 'STN', 'STNE', 'STNG', 'STNL', 'STOK', 'STON', 'STOR', 'STPP', 'STRA', 'STRL', 'STRO', 
    'STRR', 'STRT', 'STT', 'STWD', 'STX', 'STXB', 'STXS', 'SU', 'SUB', 'SUM', 'SUMO', 'SUN', 'SUNS', 'SUNW', 'SUP', 
    'SUPN', 'SUPV', 'SURF', 'SUSL', 'SUSQ', 'SVA', 'SVBI', 'SVBL', 'SVC', 'SVM', 'SVRA', 'SVT', 'SVU', 'SVVC', 'SWBI', 
    'SWC', 'SWCH', 'SWI', 'SWJ', 'SWK', 'SWM', 'SWN', 'SWP', 'SWT', 'SXC', 'SXI', 'SXT', 'SY', 'SYBT', 'SYF', 'SYK', 
    'SYKE', 'SYN', 'SYNL', 'SYPR', 'SYX', 'SYY', 'SZC', 'T', 'TA', 'TAC', 'TACT', 'TAIT', 'TAK', 'TAL', 'TALO', 
    'TANH', 'TAOP', 'TAP', 'TARA', 'TARO', 'TARS', 'TAST', 'TAT', 'TATT', 'TAYD', 'TBBK', 'TBC', 'TBI', 'TBIO', 
    'TBK', 'TBLT', 'TBNK', 'TBPH', 'TC', 'TCAP', 'TCBK', 'TCBI', 'TCBIL', 'TCBK', 'TCCO', 'TCDA', 'TCFC', 'TCF', 
    'TCFCP', 'TCGP', 'TCI', 'TCMD', 'TCRD', 'TCRX', 'TCS', 'TCX', 'TD', 'TDC', 'TDF', 'TDG', 'TDI', 'TDIV', 'TDOC', 
    'TDS', 'TDW', 'TDY', 'TEAF', 'TEAM', 'TECK', 'TEF', 'TEI', 'TEL', 'TELL', 'TEN', 'TENX', 'TEO', 'TEP', 'TER', 
    'TERM', 'TERP', 'TESS', 'TEX', 'TF', 'TFSL', 'TFX', 'TG', 'TGA', 'TGB', 'TGH', 'TGHI', 'TGI', 'TGL', 'TGNA', 
    'TGP', 'TGS', 'TGT', 'TH', 'THC', 'THG', 'THM', 'THO', 'THQ', 'THR', 'THS', 'THW', 'TIF', 'TIGO', 'TILE', 'TIPT', 
    'TISI', 'TJX', 'TK', 'TKC', 'TKR', 'TLGA', 'TLK', 'TLMD', 'TLRY', 'TLS', 'TLYS', 'TM', 'TMHC', 'TMK', 'TMO', 'TMP', 
    'TMSR', 'TMST', 'TMUS', 'TNAV', 'TNC', 'TNDM', 'TNET', 'TNP', 'TNXP', 'TOCA', 'TOL', 'TOT', 'TOUR', 'TOWN', 'TOWR', 
    'TPB', 'TPC', 'TPH', 'TPIC', 'TPL', 'TPRE', 'TPVG', 'TPX', 'TPZ', 'TR', 'TRC', 'TREX', 'TRI', 'TRIL', 'TRIP', 
    'TRK', 'TRMB', 'TRMK', 'TRMT', 'TRN', 'TRNO', 'TRNS', 'TROW', 'TROX', 'TRP', 'TRQ', 'TRS', 'TRT', 'TRTN', 'TRTX', 
    'TRU', 'TRUE', 'TRV', 'TRVG', 'TRVN', 'TRX', 'TS', 'TSBK', 'TSC', 'TSCO', 'TSE', 'TSEM', 'TSI', 'TSLA', 'TSLX', 
    'TSM', 'TSN', 'TSQ', 'TSU', 'TT', 'TTC', 'TTCF', 'TTD', 'TTEK', 'TTGT', 'TTI', 'TTM', 'TTMI', 'TTNP', 'TTOO', 
    'TTPH', 'TTSH', 'TTT', 'TTWO', 'TU', 'TUESQ', 'TUP', 'TUR', 'TURN', 'TUSA', 'TUSK', 'TV', 'TVC', 'TVE', 'TVPT', 
    'TVTY', 'TW', 'TWI', 'TWIN', 'TWLO', 'TWN', 'TWNK', 'TWO', 'TWOU', 'TWST', 'TWTR', 'TX', 'TXMD', 'TXN', 'TXRH', 
    'TXT', 'TY', 'TYG', 'TYHT', 'TYL', 'TYME', 'TZOO', 'TZP', 'U', 'UA', 'UAA', 'UAL', 'UAN', 'UBA', 'UBER', 'UBNK', 
    'UBP', 'UBS', 'UBSI', 'UBT', 'UCFC', 'UCTT', 'UDR', 'UE', 'UEC', 'UEIC', 'UEP', 'UFAB', 'UFI', 'UFS', 'UGI', 
    'UGP', 'UHAL', 'UHS', 'UHT', 'UIHC', 'UIS', 'UL', 'ULBI', 'ULH', 'ULTA', 'UMC', 'UMH', 'UMPQ', 'UN', 'UNAM', 
    'UNB', 'UNF', 'UNFI', 'UNH', 'UNIT', 'UNM', 'UNMA', 'UNP', 'UNT', 'UNTY', 'UNVR', 'UONE', 'UONEK', 'UP', 'UPLD', 
    'UPS', 'URBN', 'URGN', 'URI', 'USA', 'USAC', 'USAS', 'USB', 'USDP', 'USFD', 'USIO', 'USL', 'USLM', 'USM', 'USNA', 
    'USO', 'USPH', 'USWS', 'USX', 'UTHR', 'UTI', 'UTL', 'UTMD', 'UTSI', 'UTZ', 'UVE', 'UVSP', 'UVV', 'UWMC', 'UXIN', 
    'UZA', 'UZB', 'UZC', 'V', 'VAC', 'VALE', 'VAL', 'VALN', 'VALU', 'VAPO', 'VAR', 'VASO', 'VBIV', 'VBLT', 'VBND', 
    'VBR', 'VBTX', 'VC', 'VCEL', 'VCF', 'VCIF', 'VCLT', 'VCRA', 'VCV', 'VCYT', 'VDE', 'VEAC', 'VECO', 'VEEV', 'VEL', 
    'VER', 'VER-F', 'VER-P', 'VERU', 'VET', 'VFC', 'VG', 'VGI', 'VGIT', 'VGK', 'VGM', 'VGR', 'VGZ', 'VHC', 'VHI', 
    'VICI', 'VIPS', 'VIR', 'VIRT', 'VITL', 'VIV', 'VIVE', 'VIVO', 'VJET', 'VLO', 'VLRS', 'VLT', 'VLUE', 'VLY', 'VMAR', 
    'VMC', 'VMI', 'VMO', 'VMW', 'VNCE', 'VNDA', 'VNO', 'VNO-K', 'VNO-L', 'VNO-M', 'VNOM', 'VNRX', 'VNT', 'VOC', 
    'VOD', 'VOXX', 'VOYA', 'VPG', 'VRA', 'VREX', 'VRM', 'VRNA', 'VRNS', 'VRNT', 'VRP', 'VRS', 'VRSK', 'VRSN', 'VRT', 
    'VRTV', 'VRTX', 'VSAT', 'VSF', 'VSH', 'VSI', 'VSLR', 'VSM', 'VSS', 'VST', 'VSTO', 'VTA', 'VTGN', 'VTHR', 'VTIP', 
    'VTR', 'VTS', 'VTV', 'VTVT', 'VTWG', 'VTWO', 'VTWV', 'VUG', 'VUZI', 'VVI', 'VVNT', 'VVOS', 'VVPR', 'VVR', 'VVV', 
    'VWO', 'VXF', 'VYGR', 'VYM', 'VYMI', 'VZ', 'W', 'WAB', 'WABC', 'WAFD', 'WAL', 'WALA', 'WALD', 'WASH', 'WAT', 
    'WATT', 'WB', 'WBA', 'WBC', 'WBS', 'WBT', 'WCC', 'WCN', 'WD', 'WDAY', 'WDC', 'WDFC', 'WDR', 'WEA', 'WEC', 'WEI', 
    'WELL', 'WEN', 'WERN', 'WES', 'WETF', 'WEX', 'WEYS', 'WF', 'WFC', 'WFC-L', 'WFC-M', 'WFC-N', 'WFC-O', 'WFC-P', 
    'WFC-Q', 'WFC-R', 'WFC-T', 'WFC-V', 'WFC-W', 'WFC-X', 'WFC-Y', 'WFC-Z', 'WFG', 'WFH', 'WGO', 'WH', 'WHD', 'WHF', 
    'WHFBZ', 'WHG', 'WHLM', 'WHLR', 'WHLRD', 'WHLRP', 'WIFI', 'WILC', 'WIMI', 'WINA', 'WING', 'WINS', 'WIRE', 'WISA', 
    'WIT', 'WIX', 'WK', 'WKHS', 'WLDN', 'WLH', 'WLK', 'WLKP', 'WLL', 'WLTW', 'WM', 'WMB', 'WMC', 'WMG', 'WMK', 
    'WMS', 'WMT', 'WNC', 'WNEB', 'WNS', 'WOR', 'WORK', 'WPC', 'WPG', 'WPM', 'WPP', 'WRB', 'WRB-B', 'WRB-C', 'WRB-D', 
    'WRB-E', 'WRB-F', 'WRBY', 'WRE', 'WRI', 'WRK', 'WSBC', 'WSBF', 'WSC', 'WSFS', 'WSM', 'WSO', 'WSR', 'WST', 'WTBA', 
    'WTER', 'WTFC', 'WTFCM', 'WTI', 'WTM', 'WTRG', 'WTS', 'WTT', 'WTTR', 'WU', 'WUGI', 'WULF', 'WVE', 'WVFC', 'WVVI', 
    'WW', 'WWD', 'WWE', 'WWR', 'WWW', 'WY', 'WYNN', 'X', 'XAIR', 'XAN', 'XAN-C', 'XBI', 'XBIT', 'XBUY', 'XCOM', 'XCUR', 
    'XEL', 'XELA', 'XELB', 'XENE', 'XENT', 'XFLT', 'XFOR', 'XHB', 'XHE', 'XHR', 'XIN', 'XL', 'XLC', 'XLRN', 'XNCR', 
    'XNET', 'XOM', 'XOMA', 'XOXO', 'XPEL', 'XPER', 'XPL', 'XPO', 'XPP', 'XRAY', 'XRF', 'XRT', 'XRX', 'XSD', 'XSPA', 
    'XT', 'XTH', 'XTLB', 'XTNT', 'XU100', 'XYL', 'Y', 'YAC', 'YALA', 'YCBD', 'YCL', 'YELP', 'YETI', 'YEXT', 'YGMZ', 
    'YI', 'YIN', 'YINN', 'YJ', 'YMAB', 'YMTX', 'YNDX', 'YORW', 'YPF', 'YRCW', 'YRD', 'YSG', 'YTEN', 'YTRA', 'YUM', 
    'YUMA', 'YUMC', 'YVR', 'YY', 'Z', 'ZBH', 'ZBRA', 'ZDGE', 'ZEN', 'ZEPP', 'ZEST', 'ZETA', 'ZEUS', 'ZEV', 'ZG', 
    'ZGNX', 'ZI', 'ZIM', 'ZION', 'ZIONL', 'ZIONN', 'ZIONO', 'ZIONP', 'ZIOP', 'ZIXI', 'ZKIN', 'ZLAB', 'ZM', 'ZNGA', 
    'ZNH', 'ZNTE', 'ZNTL', 'ZOM', 'ZS', 'ZSAN', 'ZTO', 'ZTR', 'ZTS', 'ZUMZ', 'ZUO', 'ZVO', 'ZYME', 'ZYNE', 'ZYXI'
]


small_cap_tickers_less_than_50= ['AOS', 'AES', 'A', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'AMCR', 'AEE', 'AAL', 'AEP', 'AIG', 'AWK', 'AMP', 'AME', 'ANSS', 'APA', 'APTV', 'ACGL', 'ADM', 'AIZ', 'ATO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 'BK', 'BBWI', 'BAX', 'BBY', 'BIO', 'TECH', 'BIIB', 'BWA', 'BXP', 'BR', 'BRO', 'BLDR', 'BG', 'CZR', 'CPT', 'CPB', 'CAH', 'KMX', 'CCL', 'CTLT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CHRW', 'CRL', 'CHTR', 'CHD', 'CINF', 'CFG', 'CLX', 'CMS', 'CTSH', 'CAG', 'ED', 'STZ', 'COO', 'GLW', 'CPAY', 'CTVA', 'CSGP', 'CTRA', 'CCI', 'CMI', 'DRI', 'DVA', 'DAY', 'DECK', 'DAL', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DD', 'EMN', 'EBAY', 'EIX', 'EA', 'ENPH', 'ETR', 'EPAM', 'EQT', 'EFX', 'EQR', 'ESS', 'EL', 'ETSY', 'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'FFIV', 'FDS', 'FICO', 'FAST', 'FRT', 'FIS', 'FITB', 'FSLR', 'FE', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'GRMN', 'IT', 'GEHC', 'GEV', 'GEN', 'GNRC', 'GIS', 'GPC', 'GPN', 'GL', 'GDDY', 'HAL', 'HIG', 'HAS', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HOLX', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IEX', 'IDXX', 'INCY', 'IR', 'PODD', 'IFF', 'IP', 'IPG', 'IVZ', 'INVH', 'IQV', 'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JCI', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KHC', 'KR', 'LHX', 'LH', 'LW', 'LVS', 'LDOS', 'LEN', 'LYV', 'LKQ', 'L', 'LULU', 'LYB', 'MTB', 'MRO', 'MKTX', 'MLM', 'MAS', 'MTCH', 'MKC', 'MTD', 'MGM', 'MCHP', 'MAA', 'MHK', 'MOH', 'TAP', 'MPWR', 'MNST', 'MOS', 'MSCI', 'NDAQ', 'NTAP', 'NEM', 'NWSA', 'NWS', 'NI', 'NDSN', 'NTRS', 'NCLH', 'NRG', 'NUE', 'NVR', 'ODFL', 'OMC', 'ON', 'OKE', 'OTIS', 'PKG', 'PARA', 'PAYX', 'PAYC', 'PNR', 'PCG', 'PNW', 'POOL', 'PPG', 'PPL', 'PFG', 'PRU', 'PEG', 'PTC', 'PHM', 'QRVO', 'PWR', 'DGX', 'RL', 'RJF', 'O', 'REG', 'RF', 'RMD', 'RVTY', 'ROK', 'ROL', 'ROST', 'RCL', 'SBAC', 'STX', 'SRE', 'SWKS', 'SJM', 'SNA', 'SOLV', 'LUV', 'SWK', 'STT', 'STLD', 'STE', 'SYF', 'SYY', 'TROW', 'TTWO', 'TPR', 'TRGP', 'TEL', 'TDY', 'TFX', 'TER', 'TXT', 'TSCO', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'UDR', 'ULTA', 'UAL', 'URI', 'UHS', 'VLO', 'VTR', 'VLTO', 'VRSN', 'VRSK', 'VTRS', 'VICI', 'VST', 'VMC', 'WRB', 'GWW', 'WAB', 'WBA', 'WBD', 'WAT', 'WEC', 'WST', 'WDC', 'WRK', 'WY', 'WTW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH']
medium_cap_tickers_between_50_to_100= ['MMM', 'AFL', 'APD', 'ABNB', 'MO', 'AMT', 'APH', 'AON', 'AJG', 'ADSK', 'AZO', 'BDX', 'BMY', 'CDNS', 'COF', 'CARR', 'CMG', 'CI', 'CTAS', 'CME', 'CL', 'CEG', 'CPRT', 'CRWD', 'CSX', 'CVS', 'DUK', 'ECL', 'EW', 'EMR', 'EOG', 'EQIX', 'FDX', 'FI', 'FCX', 'GD', 'GM', 'GILD', 'HCA', 'HLT', 'ITW', 'ICE', 'MPC', 'MAR', 'MCK', 'MET', 'MRNA', 'MDLZ', 'MCO', 'MSI', 'NSC', 'NOC', 'NXPI', 'ORLY', 'OXY', 'PCAR', 'PH', 'PYPL', 'PSX', 'PNC', 'PSA', 'RSG', 'ROP', 'SLB', 'SHW', 'SPG', 'SO', 'SBUX', 'SMCI', 'SNPS', 'TGT', 'TT', 'TDG', 'USB', 'WM', 'WELL', 'WMB', 'ZTS']
large_cap_tickers_greater_than_100= ['ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'GOOGL', 'GOOG', 'AMZN', 'AXP', 'AMGN', 'ADI', 'AAPL', 'AMAT', 'ANET', 'T', 'ADP', 'BAC', 'BLK', 'BX', 'BA', 'BKNG', 'BSX', 'AVGO', 'CAT', 'SCHW', 'CVX', 'CB', 'CSCO', 'C', 'KO', 'CMCSA', 'COP', 'COST', 'DHR', 'DE', 'ETN', 'ELV', 'LLY', 'XOM', 'GE', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'INTU', 'ISRG', 'JNJ', 'JPM', 'KKR', 'KLAC', 'LRCX', 'LIN', 'LMT', 'LOW', 'MMC', 'MA', 'MCD', 'MDT', 'MRK', 'META', 'MU', 'MSFT', 'MS', 'NFLX', 'NEE', 'NKE', 'NVDA', 'ORCL', 'PANW', 'PEP', 'PFE', 'PM', 'PG', 'PGR', 'PLD', 'QCOM', 'RTX', 'REGN', 'SPGI', 'CRM', 'NOW', 'SYK', 'TMUS', 'TSLA', 'TXN', 'TMO', 'TJX', 'UBER', 'UNP', 'UPS', 'UNH', 'VZ', 'VRTX', 'V', 'WMT', 'DIS', 'WFC']