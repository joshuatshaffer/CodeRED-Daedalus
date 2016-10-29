using UnityEngine;
using System.Collections;
using System.IO.Ports;

public class RotateFromArd : MonoBehaviour {

	public SerialPort sp;

	public float maxSpeed = 90;
	private float angle = 0;
	private int inspeed = 0;
	// Use this for initialization
	void Start () {
		sp = new SerialPort("/dev/cu.usbmodem1411", 9600, Parity.None, 8, StopBits.One);
		sp.Open ();
		sp.ReadTimeout = 1;
	}

	// Update is called once per frame
	void Update () {
		if (sp.IsOpen) {
			try {
				inspeed = int.Parse(sp.ReadLine ());
				print (inspeed);
			} catch (System.Exception) {

			}
		}
		angle += inspeed * maxSpeed * Time.deltaTime / 1023;
		angle = Mathf.Repeat(angle, 360);
		transform.rotation = Quaternion.Euler(0, angle, 0);
	}
}
