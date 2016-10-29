using UnityEngine;
using System.Collections;

public class DropDown : MonoBehaviour {

	void Start () {
		RaycastHit hit;
		if (Physics.Raycast (transform.position, Vector3.down, out hit)) {
			transform.position = hit.point + Vector3.up * 0.5f;
		}
		Destroy (this);
	}
}
