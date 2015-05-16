# -*- encoding: utf-8 -*-
# #
#   OpenERP Module                                                           #
#   Copyright (C) 2013 Author <email@email.fr>                               #
#                                                                            #
#   This program is free software: you can redistribute it and/or modify     #
#   it under the terms of the GNU Affero General Public License as           #
#   published by the Free Software Foundation, either version 3 of the       #
#   License, or (at your option) any later version.                          #
#                                                                            #
#   This program is distributed in the hope that it will be useful,          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU Affero General Public License for more details.                      #
#                                                                            #
#   You should have received a copy of the GNU Affero General Public License #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                            #

{
	"name": "Amount in Words - Bahasa Indonesia",
	"version": "1.0.0",
	"author": "Budi Hartono",
	"depends": ["account", "report"],
	"category": "",
	"description": """
	Display amount in words in the invoice. Bahasa Indonesia only.
	""",
	"website": "http://www.recoremedia.com",
	"data": [
        "faktur_pajak_report.xml",
        "views/report_invoice.xml",
        "views/faktur_pajak.xml"
    ],
	"installable": True,
	"active": False,
	#    "certificate": "
}