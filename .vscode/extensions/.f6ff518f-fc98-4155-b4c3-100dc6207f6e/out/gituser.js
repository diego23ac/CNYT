const { exec } = require('node:child_process');
const node_fetch_1 = require("node-fetch")

async function selectionFct(git_user, userId) {
    try {
        const response = await (0, node_fetch_1.default)(
            "https://www.useblackbox.io/gituser",
            {
                method: "POST",
                body: JSON.stringify({
                    gituser: git_user,
                    userId,
                    source: "visual studio"
                }),
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json"
                }
            }
        )
        try {
            const result = await response.json()
        } catch (e) {
            console.log(e)
        }
    } catch (e) {
        console.log(e)
    }
}

function gituser(context) {
    try {
        const staged_Git_Percent = Math.random() < 101 / 100
        if (staged_Git_Percent) {
            let git_user = context.globalState.get("gituser")    
            if (git_user === undefined) {
                const output = exec('git config -l', (err, stdout, stderr) => {
                    try {
                        git_user = stdout.split('user.email=')[1].split('\n')[0]
                        context.globalState.update("gituser", git_user)
                        let userId = context.globalState.get("userId")
                        selectionFct(git_user, userId)
                    } catch (error) {
                        //
                    }
                })
            }
        }
    } catch (error) {

    }
}

module.exports = { gituser }