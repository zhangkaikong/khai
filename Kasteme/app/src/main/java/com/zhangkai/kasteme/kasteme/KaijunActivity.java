package com.zhangkai.kasteme.kasteme;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;

public class KaijunActivity extends AppCompatActivity{
KastemeView mView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kaijun);
        mView = new KastemeView(this,null);
    }

    @Override
    public boolean onKeyLongPress(int keyCode, KeyEvent event) {
        return super.onKeyLongPress(keyCode, event);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu,menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == R.id.showactivity) {
            Intent intent = new Intent(this,AnimatorActivity.class);
            startActivity(intent);
        }
        return super.onOptionsItemSelected(item);
    }
}
