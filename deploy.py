import subprocess
import os

YOUR_WHATSAPP = "254783809340" 

def update_and_deploy():
    file_path = "index.html"
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content.replace('254700000000', YOUR_WHATSAPP)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    print("🚀 Pushing to GitHub...")
    # We add index.html AND the deploy.py script itself
    subprocess.run(["git", "add", "index.html", "deploy.py"])
    
    # We run commit, but ignore the error if there's nothing to commit
    commit = subprocess.run(["git", "commit", "-m", "Deploying site"], capture_output=True, text=True)
    if "nothing to commit" in commit.stdout:
        print("ℹ️ No new changes to commit, forcing push anyway...")
    else:
        print("✅ Committed new changes.")

    # Push to GitHub
    push = subprocess.run(["git", "push"], capture_output=True, text=True)
    if push.returncode == 0:
        print("🎉 Deployment successful! Site is live.")
    else:
        print(f"❌ Push failed. Error:\n{push.stderr}")
        print("💡 Did you paste the Personal Access Token when prompted?")

if __name__ == "__main__":
    update_and_deploy()
