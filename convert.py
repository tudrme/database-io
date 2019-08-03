"""
Converts v1 database version of the Tudrme website to v2 database, using intermediatery.
"""

#!/usr/bin/python
import psycopg2
from config import config

# Generic print and exit PostgreSQL server version


def connect():
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tables(file):
    commands = (
        """
        CREATE TABLE `tutors` (
            `first_name` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
            `last_name` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `email` TEXT(320) CHARACTER SET utf8 COLLATE utf8_general_ci,
            `phone` INT unsigned,
            `grade` INT unsigned,
            `drives` BOOLEAN,
            `school` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `rate` DECIMAL unsigned zerofill,
            `sun` BOOLEAN,
            `mon` BOOLEAN,
            `tues` BOOLEAN,
            `wed` BOOLEAN,
            `thurs` BOOLEAN,
            `fri` BOOLEAN,
            `sat` BOOLEAN,
            `sun_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `mon_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `tues_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `wed_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `thurs_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `fri_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `sat_hours` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
            `early_math` BOOLEAN,
            `algebra` BOOLEAN,
            `algebra_2` BOOLEAN,
            `geometry` BOOLEAN,
            `precalculus` BOOLEAN,
            `calculus` BOOLEAN,
            `statistics` BOOLEAN,
            `early_english` BOOLEAN,
            `english_9` BOOLEAN,
            `english_10` BOOLEAN,
            `journalism` BOOLEAN,
            `debate` BOOLEAN,
            `us_history` BOOLEAN,
            `euro_history` BOOLEAN,
            `world_history` BOOLEAN,
            `economics` BOOLEAN,
            `government` BOOLEAN,
            `psychology` BOOLEAN,
            `geography` BOOLEAN,
            `earth_science` BOOLEAN,
            `physical_science` BOOLEAN,
            `life_science` BOOLEAN,
            `biology` BOOLEAN,
            `chemistry` BOOLEAN,
            `physics` BOOLEAN,
            `environmental_science` BOOLEAN,
            `forensics` BOOLEAN,
            `physiology` BOOLEAN,
            `health` BOOLEAN,
            `cpp` BOOLEAN,
            `robotics` BOOLEAN,
            `python` BOOLEAN,
            `webdev` BOOLEAN,
            `graphic_design` BOOLEAN,
            `spanish_1` BOOLEAN,
            `spanish_2` BOOLEAN,
            `spanish_3` BOOLEAN,
            `french_1` BOOLEAN,
            `french_2` BOOLEAN,
            `french_3` BOOLEAN,
            `german_1` BOOLEAN,
            `german_2` BOOLEAN,
            `german_3` BOOLEAN,
            `asl` BOOLEAN,
            `chinese_1` BOOLEAN,
            `chinese_2` BOOLEAN,
            `chinese_3` BOOLEAN,
            `japanese_1` BOOLEAN,
            `japanese_2` BOOLEAN,
            `japanese_3` BOOLEAN,
            `entrepreneurship` BOOLEAN,
            `art_history` BOOLEAN,
            `studio_art` BOOLEAN,
            `digital_art` BOOLEAN,
            `film` BOOLEAN,
            `photography` BOOLEAN,
            `ap_research` BOOLEAN,
            `ap_seminar` BOOLEAN,
            `ap_2d` BOOLEAN,
            `ap_3d` BOOLEAN,
            `ap_art` BOOLEAN,
            `ap_drawing` BOOLEAN,
            `ap_music` BOOLEAN,
            `ap_lang` BOOLEAN,
            `ap_lit` BOOLEAN,
            `ap_comp_gov` BOOLEAN,
            `ap_euro` BOOLEAN,
            `ap_macro` BOOLEAN,
            `ap_micro` BOOLEAN,
            `ap_psych` BOOLEAN,
            `ap_gov` BOOLEAN,
            `ap_us` BOOLEAN,
            `ap_world` BOOLEAN,
            `ap_human_geo` BOOLEAN,
            `ap_calc_ab` BOOLEAN,
            `ap_calc_bc` BOOLEAN,
            `ap_csa` BOOLEAN,
            `ap_csp` BOOLEAN,
            `ap_stats` BOOLEAN,
            `ap_bio` BOOLEAN,
            `ap_chem` BOOLEAN,
            `ap_enviro` BOOLEAN,
            `ap_physics_1` BOOLEAN,
            `ap_physics_2` BOOLEAN,
            `ap_physics_em` BOOLEAN,
            `ap_physics_mech` BOOLEAN,
            `ap_chinese` BOOLEAN,
            `ap_french` BOOLEAN,
            `ap_german` BOOLEAN,
            `ap_italian` BOOLEAN,
            `ap_japanese` BOOLEAN,
            `ap_latin` BOOLEAN,
            `ap_spanish_lang` BOOLEAN,
            `ap_spanish_lit` BOOLEAN,
            `prep_sat` BOOLEAN,
            `prep_act` BOOLEAN,
            `music_piano` BOOLEAN,
            `music_violin` BOOLEAN,
            `music_viola` BOOLEAN,
            `music_clarinet` BOOLEAN,
            `music_percussion` BOOLEAN,
            `music_saxophone` BOOLEAN,
            `music_oboe` BOOLEAN,
            `bio` BOOLEAN,
            `style` BOOLEAN,
            `experience` BOOLEAN
        );
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.copy_from(file, 'tutors', sep=',')
            # cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    file = open(r'Tutors.csv')
    connect()
    create_tables(file)
