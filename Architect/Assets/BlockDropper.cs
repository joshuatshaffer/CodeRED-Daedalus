using UnityEngine;
using System.Collections;

public class BlockDropper : MonoBehaviour {

	public GameObject blockL, blockD;
	public GameObject[,,] blocks;
	public Transform goestBlock;
	public int buildSizeX = 12;
	public int buildSizeY = 12;
	public int buildSizeZ = 12;

	void Start () {
		blocks = new GameObject[buildSizeX, buildSizeY, buildSizeZ];
	}
	
	void Update() {
		RaycastHit hit;

		if (Physics.Raycast(Camera.main.ScreenPointToRay(new Vector3(Screen.width / 2,Screen.height / 2,0f)), out hit, 100)) {
			Vector3 poinerPosition = hit.point + hit.normal * 0.5f;
			int ppx = Mathf.RoundToInt (poinerPosition.x+6);
			int ppy = Mathf.RoundToInt (poinerPosition.y);
			int ppz = Mathf.RoundToInt (poinerPosition.z+6);
			if (ppx < 0 || ppy < 0 || ppz < 0 || ppx >= 12 || ppy >= 12 || ppz >= 12) {
				goestBlock.gameObject.SetActive (false);
				return;
			} else {
				goestBlock.gameObject.SetActive (true);
			}
			poinerPosition = new Vector3 (ppx-6,ppy,ppz-6);

			if (Input.GetMouseButtonDown (1)) {
				Debug.Log (ppx + ppy + ppz);
				GameObject newBlock = (GameObject)Instantiate ((((ppx+ppy+ppz) & 1) == 0) ? blockL : blockD, poinerPosition, Quaternion.identity);
				blocks [ppx, ppy, ppz] = newBlock;
			} else if (Input.GetMouseButtonDown (0)) {
				Destroy (blocks [ppx - Mathf.RoundToInt(hit.normal.x),
					ppy - Mathf.RoundToInt(hit.normal.y),
					ppz - Mathf.RoundToInt(hit.normal.z)]);
			} else {
				goestBlock.position = poinerPosition;
			}
		}
		if (Input.GetButtonDown ("WriteBlueprint")) {
			OutputToFile ("../blueprint.txt");
		}
	}

	string BlocksToString() {
		string output = "";
		for (int y=0; y < buildSizeY; ++y) {
			if (y > 0)
				output += "\n--\n";
			for (int z = 0; z < buildSizeZ; ++z) {
				if (z > 0)
					output += '\n';
				for (int x=0; x < buildSizeX; ++x) {
					if (x > 0)
						output += ',';
					output += blocks [x, y, z] != null ? '1' : '0';
				}
			}
		}
		return output;
	}

	void OutputToFile (string filename) {
		System.IO.File.WriteAllText(filename,BlocksToString());
	}
}
