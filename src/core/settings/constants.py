# coding=utf-8
from collections import OrderedDict
from core.conf.utils import map_industries

ALL_INDUSTRIES = ('all', 'all')

HIERARCHICAL_INDUSTRIES = OrderedDict([
    ('afs', ('Accommodation and food service', None)),
    ('aer', ('Arts, entertainment & recreation', None)),
    ('co', ('Construction', None)),
    ('edu', ('Education', OrderedDict([
        ('edu-fe', ('Further education', None)),
        ('edu-o', ('Other', None)),
        ('edu-pe', ('Primary education', None)),
        ('edu-se', ('Secondary education', None)),
    ]))),
    ('egsw', ('Electricity, gas, steam, water', None)),
    ('fi', ('Financial and Insurance', OrderedDict([
        ('fi-b', ('Banking', None)),
        ('fi-i', ('Insurance', None)),
        ('fi-o', ('Other', None)),
    ]))),
    ('hh&sw', ('Human health & social work', None)),
    ('ic', ('Information and Communication', OrderedDict([
        ('ic-bnpj', ('Books, news, periodicals, journals', None)),
        ('ic-o', ('Other', None)),
        ('ic-s', ('Software', None)),
        ('ic-trmvm', ('TV, radio, movies, video, music', None)),
        ('ic-t', ('Telecommunications', None)),
    ]))),
    ('ma', ('Manufacturing', OrderedDict([
        ('ma-c', ('Chemicals', None)),
        ('ma-ctd', ('Cosmetics, toiletries, detergents', None)),
        ('ma-e', ('Electronics', None)),
        ('ma-fb', ('Food & beverages', None)),
        ('ma-f', ('Furniture', None)),
        ('ma-me', ('Machinery & equipment', None)),
        ('ma-o', ('Other', None)),
        ('ma-p', ('Pharmaceuticals', None)),
        ('ma-tfa', ('Textiles, footwear & apparel', None)),
        ('ma-tg', ('Toys & games', None)),
        ('ma-v', ('Vehicles', None)),
    ]))),
    ('other', ('Other service activities - Other', None)),
    ('os-p', ('Other service activities - Printing', None)),
    ('pa', ('Professional activities', OrderedDict([
        ('pa-c', ('Consultancy', None)),
        ('pa-l', ('Legal', None)),
        ('pa-o', ('Other', None)),
        ('pa-r', ('Research', None)),
    ]))),
    ('papo', ('Public administration & political organisations', None)),
    ('re', ('Real estate', None)),
    ('rt', ('Retail trade', OrderedDict([
        ('r-mc', ('Multi-category', None)),
        ('rt-bmv', ('Books, music, video', None)),
        ('rt-c', ('Chemicals', None)),
        ('rt-ctd', ('Cosmetics, toiletries, detergents', None)),
        ('rt-e', ('Electronics', None)),
        ('rt-fb', ('Food and beverages', None)),
        ('rt-f', ('Furniture', None)),
        ('rt-hg', ('Household goods', None)),
        ('rt-me', ('Machinery & equipment', None)),
        ('rt-o', ('Other', None)),
        ('rt-p', ('Pharmaceuticals', None)),
        ('rt-tfa', ('Textiles, footwear & apparel', None)),
        ('rt-tg', ('Toys & games', None)),
        ('rt-v', ('Vehicles', None)),
    ]))),
    ('tt', ('Transportation and Travel', OrderedDict([
        ('tt-o', ('Other', None)),
        ('tt-rflw', ('Railway, flight, land & water transport', None)),
        ('tt-tato', ('Travel agency & tour operator', None)),
    ]))),
    ('wt', ('Wholesale trade', OrderedDict([
        ('wt-bmv', ('Books, music, video', None)),
        ('wt-c', ('Chemicals', None)),
        ('wt-ctd', ('Cosmetics, toiletries, detergents', None)),
        ('wt-e', ('Electronics', None)),
        ('wt-fb', ('Food and beverages', None)),
        ('wt-f', ('Furniture', None)),
        ('wt-hg', ('Household goods', None)),
        ('wt-me', ('Machinery & equipment', None)),
        ('wt-o', ('Other', None)),
        ('wt-p', ('Pharmaceuticals', None)),
        ('wt-tfa', ('Textiles, footwear & apparel', None)),
        ('wt-tg', ('Toys & games', None)),
        ('wt-v', ('Vehicles', None)),
    ]))),
])

INDUSTRIES = map_industries(HIERARCHICAL_INDUSTRIES, None, {})

COUNTRIES = OrderedDict([
    ('AF', 'Afghanistan'),
    ('AX', 'Åland Islands'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua and Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia, Plurinational State of'),
    ('BQ', 'Bonaire, Sint Eustatius and Saba'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('IO', 'British Indian Ocean Territory'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Republic'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos (Keeling) Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CD', 'Congo, the Democratic Republic of the'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Côte d\'Ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CW', 'Curaçao'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French Southern Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GG', 'Guernsey'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HM', 'Heard Island and McDonald Islands'),
    ('VA', 'Holy See (Vatican City State'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran, Islamic Republic of'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IM', 'Isle of Man'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JE', 'Jersey'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea, Democratic People\'s Republic of'),
    ('KR', 'Korea, Republic of'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Lao People\'s Democratic Republic'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macao'),
    ('MK', 'Macedonia, the former Yugoslav Republic of'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia, Federated States of'),
    ('MD', 'Moldova, Republic of'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('ME', 'Montenegro'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PS', 'Palestinian Territory, Occupied'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Réunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('BL', 'Saint Barthélemy'),
    ('SH', 'Saint Helena, Ascension and Tristan da Cunha'),
    ('KN', 'Saint Kitts and Nevis'),
    ('LC', 'Saint Lucia'),
    ('MF', 'Saint Martin (French part'),
    ('PM', 'Saint Pierre and Miquelon'),
    ('VC', 'Saint Vincent and the Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome and Principe'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('RS', 'Serbia'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SX', 'Sint Maarten (Dutch part'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('SS', 'South Sudan'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SJ', 'Svalbard and Jan Mayen'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan, Province of China'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania, United Republic of'),
    ('TH', 'Thailand'),
    ('TL', 'Timor-Leste'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TC', 'Turks and Caicos Islands'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('UM', 'United States Minor Outlying Islands'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VE', 'Venezuela, Bolivarian Republic of'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands, British'),
    ('VI', 'Virgin Islands, U.S'),
    ('WF', 'Wallis and Futuna'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
])
