# mailproxy
mailproxy is a simple SMTP proxy. It receives emails through an unencrypted, unauthenticated SMTP interface and retransmits them through a remote SMTP server that requires modern features such as encryption (SSL, STARTTLS) and/or authentication (SMTP AUTH). mailproxy is primarily useful for enabling email functionality in legacy software that only supports plain SMTP.

# Requirements
* Python 3.5+
* [aiosmtpd 1.1+](https://aiosmtpd.readthedocs.io)

1. Create a virtualenv on python3.5 and switch to it.
	# mkvirtualenv -p $(which python3.5) mailproxy
	# workon mailproxy
2. Install requirements: pip install -r requirements.txt
3. Create a config file from config.ini.sample as config.ini
4. Run mailproxy from the command line, e.g. `python mailproxy.py`.

By default, mailproxy looks for a `config.ini` in its own directory.
If you have placed your config file elsewhere, you can run mailproxy
using `python mailproxy.py <config_file_path>`.
