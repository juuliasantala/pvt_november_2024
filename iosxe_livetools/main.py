from flask import Flask, render_template, redirect, url_for
from dotenv import dotenv_values

import livetools_functions


env = dotenv_values(".env")
DEVICE = {
    "host": env["HOST"],
    "user": env["USERNAME"],
    "pw": env["PASSWORD"]
}

tests = {
    "ping": {"job_id": None, "status": None, "target_ip": None},
    "traceroute": {"job_id": None, "status": None, "target_ip": None},
}

app = Flask(__name__)

@app.route("/")
def dashboard():
    print(f"{tests=}")
    return render_template("index.html", device=DEVICE["host"], tests=tests, results=None)

@app.route("/ping", methods=["POST"])
def ping():

    print(f"Pinging target: {target}")
    job_id = livetool_functions.ping_action(DEVICE["host"], DEVICE["user"], DEVICE["pw"], target)
    tests["ping"]["job_id"] = job_id
    tests["ping"]["target_ip"] = target

    return redirect(url_for('dashboard'))

@app.route("/ping_result/<job_id>", methods=["GET"])
def ping_results(job_id):
    print(f"Getting ping_result: {job_id}")
    results = livetool_functions.ping_results(DEVICE["host"], DEVICE["user"], DEVICE["pw"], job_id)

    print(f"{tests=}")
    return render_template("index.html", device=DEVICE["host"], tests=tests, results=results)

@app.route("/traceroute", methods=["POST"])
def traceroute():

    print(f"Tracerouting to target: {target}")
    job_id = livetool_functions.traceroute_action(DEVICE["host"], DEVICE["user"], DEVICE["pw"], target)
    tests["traceroute"]["job_id"] = job_id
    tests["traceroute"]["target_ip"] = target

    return redirect(url_for('dashboard'))

@app.route("/traceroute_result/<job_id>", methods=["GET"])
def traceroute_results(job_id):
    print(f"Getting traceroute_result: {job_id}")
    results = livetool_functions.traceroute_results(DEVICE["host"], DEVICE["user"], DEVICE["pw"], job_id)

    print(f"{tests=}")
    return render_template("index.html", device=DEVICE["host"], tests=tests, results=results)
